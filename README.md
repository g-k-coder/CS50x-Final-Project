# Done
## Video Demo:  [https://youtu.be/nLg4EYivbpk](https://youtu.be/nLg4EYivbpk)
## About project
This is my CS50x final project. I often forget to do simple errands or to do something.
The very simple goal of a to-do list is to get my tasks done; often it is a simple activity like putting your sheets back on the bed or booking my next trip. Often a list is all that is necessary to meet that simple goal.
The best way to manage a list is simply to put everything on the list as a priority to do. If it is something you had to do, and it took me a minute to get that done, it should be marked as a basic task; in this way, everything is a priority.
<br/>
<br/>

DONE is a web application that works as a To-Do list.
<br/>
The functionalities of the application are:

- Registration: Mandatory, functionalities of the application are available only if the user is registered.
- Password change: After registering, users can alter their password only if the current password is provided.
- Add: Append the new item to the ToDo list.
- Edit: After adding an item to the list, the user can edit it.
- Done: Removes the item from the list.
<br/>

## Prerequisites

What things you need to install the software and how to install them.<br/>
A *step-by-step* instructions that tell you how to get the project running.

Open your terminal and follow the instructions:

```
# Instructions are for Debian-Ubuntu Operating Systems

$ sudo apt update && sudo apt upgrade
# Downloads and installs the updates for each outdated package and dependency on your system

$ sudo apt-get install python3 python3-dev
# Downloads and installs the latest version of Python 3

$ sudo apt-get install python3-pip
# Downloads and installs the PIP

$ pip3 install Flask
# Downloads and installs Flask

$ pip3 install Flask-Session
# Downloads and installs Flask-Session
# Flask-Session adds server-side session support to Flask application

$ sudo apt install sqlite3
# Downloads and installs SQLite3

$ pip3 install cs50
# Downloads and installs CS50 library for Python

$ sudo pip3 install style50
# Downloads and installs style50 for Python

$ sudo apt-get install astyle
# Downloads and installs Artistic Style

$ sudo pip install --upgrade style50
# Upgrades style50
```
<br/>

- [Python Documentation](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Pip Documentation](https://pypi.org/project/pip/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/installation/#install-flask)
    - [Flask Dependencies Automatically Installed with Flask](https://flask.palletsprojects.com/en/2.2.x/installation/#dependencies)
        * [Werkzeug](https://palletsprojects.com/p/werkzeug/) implements WSGI, the standard Python interface between applications and servers.
        * [Jinja](https://palletsprojects.com/p/jinja/) is a template language that renders the pages your application serves.
        * [MarkupSafe](https://palletsprojects.com/p/markupsafe/) comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
        * [ItsDangerous](https://palletsprojects.com/p/itsdangerous/) securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
        * [Click](https://palletsprojects.com/p/click/) is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.

    - [Optional Dependencies](https://flask.palletsprojects.com/en/2.2.x/installation/#optional-dependencies)
        * [Blinker](https://pythonhosted.org/blinker/) provides support for [Signals](https://flask.palletsprojects.com/en/2.2.x/signals/).
        * [python-dotenv](https://github.com/theskumar/python-dotenv#readme) enables support for Environment Variables From dotenv when running flask commands.
        * [Watchdog](https://pythonhosted.org/watchdog/) provides a faster, more efficient reloader for the development server.

- [SQLite Documentation](https://www.sqlite.org/download.html)
- [CS50 Library for Python Documentation](https://cs50.readthedocs.io/libraries/cs50/python/)
- [Style50 Documentation](https://cs50.readthedocs.io/style50/#)
- [Artistic Style Documetation](https://astyle.sourceforge.net/)

<br/>


### Prerequisites - Recommendation
- [Visual Studio Code Download](https://code.visualstudio.com/#alt-downloads)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)

[Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code), also commonly referred to as VS Code, is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux and macOS. Features include support for debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git.
(*source: **Wikipedia***)

<br/>

## Cloning

Copy and paste `git --version` to your terminal to check if you have Git installed on your system.
<br/>
If your terminal returns a Git version as an output, that confirms you have Git installed on your system and you can skip the first step below.
<br/>
If not, you have to download and install Git.

```
$ sudo apt-get install git
# Downloads and installs Git

$ git clone https://github.com/g-k-coder/project-50.git
# Clones the GitHub repository to your machine
```
<br/>

## Coding style test

Check if the code is aesthetically pleasing and easy to read.
Navigate to the project's directory, open terminal and follow the instructions below:
```
$ style50 *.py
```

```
# Example

$ style50 *.py
Results generated by style50 v2.7.5
::::::::::::::
app.py
::::::::::::::
Looks good!
But consider adding more comments!
::::::::::::::
helpers.py
::::::::::::::
Looks good!
But consider adding more comments!
```

<br/>

## Deployment

How to deploy this on a live system:
Navigate to the project's directory, open terminal and follow the instructions below:
```
$ export FLASK_APP=app.py
$ flask run
```
<br/>

## Built With

* [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Web framework
* [Python 3](https://www.python.org/) - Programming language
* [HTML5](https://html.com/) - Markup Language
* [CSS](https://htmlcheatsheet.com/css/) - Style Sheet Language
* [Bootstrap](https://getbootstrap.com/) - CSS Framework
* [SQL](https://www.w3schools.com/sql/) - Query Language For Database Manipulation
* [CS50](https://cs50.readthedocs.io/libraries/cs50/python/) - CS50's Library For Python

<br/>

## Succint project breakdown per file

- ["static" directory](project/static) - contains static files such as CSS files, JavaScript files and images
    - [logo_icon.ico](project/static/logo_icon.ico) - icon displayed in the HTML head, i.e., browser tab
    - [style.css](project/static/styles.css) - CSS file defining the look-and-feel of each web page, i.e., each HTML file
- ["templates" directory](project/templates) - contains only HTML documents
    - [edit.html](project/templates/edit.html) - web page where users modify their tasks on the To-Do list
    - [error.html](project/templates/error.html) - displays the image and the text of an error which caused them to be redirected to this page
    - [index.html](project/templates/index.html) - "homepage"
    - [layout.html](project/templates/layout.html) - skeletal structure of the web page, in order to keep the code in the DRY principle
    - [login.html](project/templates/login.html) - users input their username and password
    - [password_change.html](project/templates/password_change.html) - allows the users to change their password
    - [register.html](project/templates/register.html) - page containing username field, and two password fields, so that users can confirm their password
    - [todo.html](project/templates/todo.html) - the web page where most of the web application functionalities happen, e.g. add to the list, remove from it, edit the items on the list
- [app.py](project/app.py) - Python code making all of the functionalities happen
- [done.db](project/done.db) - Relational database containing tables of users, and their To-Do lists
- [helpers.py](project/helper.py) - Ensures that user is logged in and checks for errors
- [requirements.txt](project/requirements.txt) - Text file containing the list of all Python libraries and modules imported in the Python code

<br/>
<br/>

## Author of the project
* **Gabriel Alfred Krupa** - [g-k-coder](https://github.com/g-k-coder)

## Author of the template
* **Billie Thompson** - [A good README template](https://github.com/PurpleBooth/a-good-readme-template) - [PurpleBooth](https://github.com/PurpleBooth)

    ## License
    This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/PurpleBooth/a-good-readme-template/blob/main/LICENSE.md) file for details
