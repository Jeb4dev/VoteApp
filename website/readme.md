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
git clone repo_url.git
```

After cloning or downloading this git repo, install required python libraries

```sh
pip install requirements.txt
```

For production environments...


## Development

Want to contribute? Great!
Give feedback, suggest new features, maybe even create pull request.


#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Credits
- [GrapesJS] - Building templates without codings!
- [Coolors] - Color palette for pie diagram.
- [Dillinger] - Template for readme.md



## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [GrapesJS]: <https://grapesjs.com/>
   [Coolors]: <https://coolors.co/>
   [Dillinger]: <https://dillinger.io/>
