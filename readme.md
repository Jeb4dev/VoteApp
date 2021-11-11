# VoteApp
## _Simple voting web app made with python_

[![N|Solid](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)](https://flask.palletsprojects.com/en/2.0.x/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

VoteApp is simple online voting web app made for pc, mobile browsing will not be great. 
This was made as part of the weekly programming challenge hosted by [DevJam](https://discord.gg/CCJvVD3Edr).
The project was made for learning purposes.

## Features

- Vote as guest or create account
- Create votes yourself
- decide if users must be authenticated to vote 
- see what others have voted
- vote results are shown as pie diagram

Creating New Vote
![image](https://user-images.githubusercontent.com/76889226/141230845-2ed34f77-4eaf-4bc5-be6a-ccccb4e4fd25.png)

Vote Results
![image](https://user-images.githubusercontent.com/76889226/141230928-fc12eaec-8353-4ddb-a122-9c3b9a7d2546.png)


## Tech

Python libraries that VoteApp uses:

- [Flask] - Micro web framework
- [Flask login] - provides user session management for Flask.
- [Flask-SQLAlchemy] - adds support for SQLAlchemy.
- [matplotlib] - data visualization with Python


## Installation

VoteApp requires [python 3.7+](https://www.python.org/downloads/) to run.

Clone git repo
```sh
git clone https://github.com/JesperKauppinen/VoteApp.git
```

After cloning or downloading this git repo, install required python libraries

```sh
pip install -r requirements.txt
```

run main.py
```sh
python3 main.py
```


## Development

Want to contribute? Great!
Give feedback, suggest new features, maybe even create pull request.


## Credits
- [GrapesJS] - Building templates without codings!
- [Coolors] - Color palette for pie diagram.
- [Dillinger] - Template for readme.md



## License

MIT

   [GrapesJS]: <https://grapesjs.com/>
   [Coolors]: <https://coolors.co/>
   [Dillinger]: <https://dillinger.io/>
   [Flask]: <https://flask.palletsprojects.com/en/2.0.x/>
   [Flask login]: <https://flask-login.readthedocs.io/en/latest/>
   [Flask-SQLAlchemy]: <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>
   [matplotlib]: <https://matplotlib.org/>
