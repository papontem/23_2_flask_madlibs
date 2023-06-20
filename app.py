# this is app.py
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import *

#flask requiered app name
app = Flask(__name__)

#flask debugtoolbar
app.config['SECRET_KEY'] = "oh-so-secret-secret-key-is-secret"
debug = DebugToolbarExtension(app) 


@app.route('/') #decorator expecting a function
def homepage(): #the function that will be executed when decorator is flagged
    """Show homepage"""

    prompts = story.prompts
    print(f"prompts from our story instance: {prompts}")

    # this didnt work, cant use {%%} blocks outside of templates for jinja to read.
    html = f"""
    <html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		
		<!--V-ANIMATED-Tab-Icon-V-->
		<link rel="icon" type="gif" href="/static/pam_favicon_animated.gif" />

		<title> FlaskMadlibs Homepage </title>
	</head>
        <body>
            <main>
                <header>
                    <h1>Home</h1>
                    <p>Welcome to this simple Flask Madlibs app</p>
                </header>
                <hr/>
                <h1>Madlibs form</h1>
                <form action="/story">
                    <!-- this should render all of the prompets that are inside of the provided default Stories' class instance story -->
        """
    # Add as many propmts as requiered from built in story instance attribute prompts
    for prompt in prompts:
        html = html + f"""
        <label for="{prompt}">{prompt}</label>
        <input type="text" placeholder="{prompt}" name="{prompt}" />
        <br><br>
        """
    html=html + """                    <button>Submit!</button>
                </form>
                <hr/>
                <footer>
				<section class="Footer_Content">
					<p>&copy; Phedias A.M. All Rights Reserved</p>
				</section>
			</footer>
            </main>
        </body>
    </html>
    """
    return html

@app.route("/story")
def home_form_submit_show_story_HTML_():
    """Handle request to show the story like /story?prompt=<prompt_value>&prompt=<prompt_value>&...."""

    prompts = story.prompts
    sent_data = request.args
    answers = {} 
    # answers = [request.args[prompt] for prompt in prompts]

    for prompt in prompts:
        if request.args[prompt] != '':
            answers[prompt] = request.args[prompt]
        else:
            answers[prompt] = prompt

    result = story.generate(answers)
    

    html = f"""
    <html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		
		<!--V-ANIMATED-Tab-Icon-V-->
		<link rel="icon" type="gif" href="/static/pam_favicon_animated.gif" />

		<title> Story </title>
	</head>
        <body>
            <main>
                <header>
                    <h1>Story</h1>
                    <p> Here is your story</p>
                </header>
                <hr/>
                <main>
                    <p>
                        <!-- gonna put story here: -->
                        <blockquote>
                            {result}
                        </blockquote>
                        <!-- sent data: <blockquote>{sent_data}</blockquote> -->
                        <!-- answers: <blockquote>{answers}</blockquote> -->
                    </p>
                </main>
                <hr/>
                <footer>
				<section class="Footer_Content">
					<p>&copy; Phedias A.M. All Rights Reserved</p>
				</section>
			</footer>
            </main>
        </body>
    </html>
    """
    return html