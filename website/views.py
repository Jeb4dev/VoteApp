from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user

from json import dumps, loads
from matplotlib import pyplot as plotter
from matplotlib import use


from . import db
from .models import Vote


"""     This file handle vote logic:
        Showing landing page,
        creating new votes, voting,
        showing vote results. """


views = Blueprint('views', __name__)
use('Agg')


# Landing Page
@views.route('/', methods=['GET'])
def home():

    # ip = request.remote_addr

    # Check if user is mobile and tell this is not made for mobile
    user_agent = request.headers.get('User-Agent')
    if 'mobile' in user_agent.lower():
        flash('This website is not made for mobile. It should still work, just expect some zooming', category='error')
        #  TODO: maybe another template for mobile users

    vote_objects = Vote.query.all()
    most_popular = []
    for i in range(len(vote_objects)):
        most_popular.append((vote_objects[i], int(vote_objects[i].popularity)))
    most_popular_sortted = sorted(most_popular, key=lambda x: (int(x[1])), reverse=True)
    most_popular_limited = most_popular_sortted[0:10]
    if request.method == "GET":
        return render_template("index.html", vote=most_popular_limited)


# Creating new vote
@views.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        question = str(request.form.get('question'))
        auth_req = str(request.form.get('auth_required'))

        # Check if auth will be required and set that to boolean
        require_auth = False
        if auth_req == "on":
            require_auth = True

        answers = []
        for i in range(10):
            answer = request.form.get(f'ans{i}')
            if not answer: break
            answers.append(answer)

        answers_in_json = dumps(answers)
        if current_user.is_authenticated:
            creator = current_user.username
        else:
            creator = "Guest"
        new_vote = Vote(question=question, answers=answers_in_json, creator=creator, auth_required=require_auth)
        db.session.add(new_vote)
        db.session.commit()
        vote_id = new_vote.id
        flash('Vote created!', category='success')
        return redirect(url_for('views.vote', vote_id=vote_id))
    return render_template("create.html", user=current_user)


# Voting page
@views.route('/votes/<vote_id>', methods=['GET', 'POST'])
def vote(vote_id):

    voteobj = Vote.query.filter_by(id=vote_id).first()
    answerlist = loads(voteobj.answers)
    user_answers = loads(voteobj.user_answers)
    total_votes = voteobj.popularity

    # Check if singed in and already voted
    voted = False
    if current_user.is_authenticated:
        if sum(row.count(str(current_user.username)) for row in user_answers) > 0:
            voted = True

    # This list will include user answer and user name. It will be added to all answers list.
    users_answer = []

    # if sending post request (voting results)
    if request.method == "POST":

        # redirect user to results if user was already voted
        if request.form.get('check-results') == "yes":
            return redirect(url_for('views.result', vote_id=vote_id))

        # define name of voter
        if current_user.is_anonymous:
            guest_name = request.form.get('voter')
            if guest_name:
                voter_name = f"{guest_name} (guest)"
            else:
                flash("You must include your name in order to vote as guest (not signed in)", category="error")
                return redirect(url_for('views.vote', vote_id=vote_id))
        elif current_user.is_authenticated:
            voter_name = current_user.username

        # loop throw all possible answers and get answer that user chose, then break
        answer = None
        for i in range(10):
            if str(request.form.get(f'ans{i}')) != "None":
                answer = str(request.form.get(f'ans{i}'))
                break
        # user_answer is [answer_num, voter_name]
        users_answer.append(answer)
        users_answer.append(voter_name)

        # add user_answer to list of all answers and change it back to json format
        user_answers.append(users_answer)
        user_answers_in_json = dumps(user_answers)

        # total votes += 1
        new_total_votes = total_votes + 1

        # update vote obj in db with new voters answers and commit changes to db
        voteobj.user_answers = user_answers_in_json
        voteobj.popularity = new_total_votes
        db.session.commit()

        # notify user, that everything vent right
        flash('Voted Successfully!', category='success')

        # render result page
        return redirect(url_for('views.result', vote_id=vote_id))
    return render_template("vote.html", user=current_user, question=voteobj.question, answerlist=answerlist,
                           voted=voted, creator=voteobj.creator, auth_required=voteobj.auth_required)


# All votes page
@views.route('/votes', methods=['GET'])
def votes():
    vote_objects = Vote.query.all()
    return render_template("votes.html", vote=vote_objects)


# Result page
@views.route('/result/<vote_id>', methods=['GET'])
def result(vote_id):
    # Define db object
    vote_object = Vote.query.filter_by(id=vote_id).first()

    # individuals with their votes  [name, answer]
    users_votes = []

    # json -> list
    answerlist = loads(vote_object.answers)
    original_answerlist = loads(vote_object.answers)
    user_answers = loads(vote_object.user_answers)

    # Append answers and names to users_votes
    for i in range(len(user_answers)):
        user_answer = answerlist[int(user_answers[i][0])]
        user_name = user_answers[i][1]
        users_votes.append((user_name, user_answer))

    pie_labels = answerlist

    # Create list with len of asnwers  like [0, 0, 0, 0, 0, 0]
    answer_share = [0] * len(answerlist)

    answer_share_real = []

    # Iterate throw answer list and calculate answers per option
    for i in range(len(answerlist)):
        num = sum(row.count(str(i)) for row in user_answers)
        if num > 0:
            answer_share_real.append(num)
        else:
            pie_labels[i] = None

    while None in pie_labels:
        pie_labels.remove(None)

    pie_labels = tuple(pie_labels)

    figure_object, axes_object = plotter.subplots()

    # Colors for
    """cmap = ['#DEC9E9', '#6247AA', '#7251B5', '#DAC3E8', '#D2B7E5', '#815AC0', '#C19EE0', '#9163CB', '#B185DB', '#A06CD5'] # purplish
    cmap = ['#f94144', '#f3722c', '#f8961e', '#f9844a', '#f9c74f', '#90be6d', '#43aa8b', '#4d908e', '#577590', '#277da1'] # colorful
    cmap = ['#FFCCCC', '#FABBBB', '#FFAAAA', '#FA9999', '#FF8888', '#FA7777', '#FF6666', '#FA5555', '#FF4444', '#FA3333'] # red ish
    cmap = ['#03071E', '#370617', '#6A040F', '#9D0208', '#D00000', '#DC2F02', '#E85D04', '#F48C06', '#FAA307', '#FFBA08'] # german"""
    cmap = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF', '#A0C4FF', '#BDB2FF', '#FFC6FF', '#E58C8A', '#ff6961'] # pastel

    if len(answer_share_real) > 0:
        # Draw the pie chart
        patches, texts, pcts = axes_object.pie(answer_share_real,
                                               labels=pie_labels,
                                               autopct='%1.2f%%',
                                               startangle=90,
                                               shadow=False,
                                               colors=cmap)

        # define label colors and boldness

        plotter.setp(texts, color='white')
        plotter.setp(pcts, color='black')
        plotter.suptitle("Options: " + ", ".join(original_answerlist), color='white')
    else:
        axes_object.pie([0])
        plotter.suptitle("Options: " + ", ".join(original_answerlist), color='white')
        plotter.title("There are total of 0 answers given.", color='white')

    # Aspect ratio - equal means pie is a circle
    axes_object.axis('equal')
    plotter.savefig('static/images/result.png', transparent=True)
    plotter.close()

    return render_template("result.html", vote=vote_object, users_and_votes=users_votes)
