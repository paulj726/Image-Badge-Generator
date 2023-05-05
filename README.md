Badge Creator App
===================

This is the Badge Creator app. To run the app on Replit, follow these steps:

1. Clone this repository on your local machine.
2. Open Replit and create a new project.
3. Import the cloned repository to the Replit project by using the import functionality on the left sidebar.
4. Create a virtual environment by running `virtualenv venv` command.
5. Activate the virtual environment by running `source venv/bin/activate` command.
6. Install the required packages using the command `pip install -r requirements.txt`.
7. Export Flask app by running `export FLASK_APP=app.py` command.
8. Run the app locally by running `flask run` command.
9. In the console, look for the URL provided for where to access the badge creator app. You can click on that URL to access the Flask web app.

### Files and their descriptions

1. app.py - Main Flask application
2. static/
    - styles.css: CSS styling for the web app
    - emboss.png: Embossed texture image
3. templates/
    - index.html: HTML template for the web app
    - badge.html: HTML template for badge image
4. requirements.txt - List of Python packages required to run the app
5. README.md - This file, containing instructions and descriptions of the files in the repository.
