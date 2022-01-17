# Module imports
from flask import Flask, render_template, url_for, redirect, request 
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_mysqldb import MySQL 
import pymysql
import pymysql.cursors

# file imports
from sqlconf import conf # connect with pymysql from config file
from dictsearch import searchdict


#######################################################
# run sudo yum install -y mysql-devel on the instance #
#######################################################

# create application function
def create_app():
    application = Flask(__name__)
    FontAwesome(application)
    application.config['SECRET_KEY'] = 'Corallivore33' #need for search

    # application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1 

    return application

# instantiate app and MySQL
application = create_app()
mysql = MySQL(application)


# create pymysql cursor to interact with MySQL database
def createCursor():
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    return cursor

######## VIEWS ###########
# define actions for home page
@application.route('/', methods=['GET', 'POST'])
def index():

    cursor=createCursor()
    defsdata=cursor.execute("SELECT * FROM CoralDefinitions")
    defsdata = cursor.fetchall() # makes selection iterable
    cursor.close()

    return render_template('index.html', defsdata=defsdata, )


# actions for search page   
@application.route('/search', methods=['GET', 'POST'])
def search():

    # create variables for each search option
    params = request.form.get('search')
    tqry = request.form.get('onlyterms')
    dqry= request.form.get('onlydefs')   
    
    # response if no matches found
    nomatch = f"No results for {params} found"

    # column selection from db written longhand as variable assignment 
    # causes empty results
    
    # perform search according to options
    if request.method == "POST":

        results = searchdict(params,tqry,dqry)
    else:pass
            
    return render_template('searchpage.html', nomatch=nomatch, results=results)
        
# define action for contributor page
@application.route('/contributors')
def contributors():

    cursor=createCursor()
    contributors=cursor.execute("SELECT * FROM Contributors")
    contributors = cursor.fetchall() # makes selection iterable
    cursor.close()

    return render_template('contributors.html', contributors=contributors)

# define action for about page
@application.route('/about')
def about():
    return render_template('aboutme.html')

# define action for contcact page
@application.route('/contact')
def contact():
    return render_template('contact.html')


# # No caching at all for API endpoints.
# @application.after_request
# def add_header(response):
#     # response.cache_control.no_store = True
#     if 'Cache-Control' not in response.headers:
#         response.headers['Cache-Control'] = 'no-store'
#     return response

if __name__ == "__main__":
    application.run(debug=True)

    # export FLASK_APP=application.py