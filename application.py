from flask import Flask, render_template, url_for, redirect, request 
#from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import SubmitField

def create_app():
    application = Flask(__name__)
    #FontAwesome(application)
    application.config['SECRET_KEY'] = 'change this unsecure key' #need for search
    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    return application


application = create_app()

# define action for home page
@application.route('/')
def index():
    return render_template('index.html')


# No caching at all for API endpoints.
@application.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
    application.run(debug=True)