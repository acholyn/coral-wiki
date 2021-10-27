# Module imports
from flask import Flask, render_template, url_for, redirect, request 
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_mysqldb import MySQL 
import pymysql
import pymysql.cursors

# connect with pymysql from config file
from sqlconf import conf

#######################################################
# run sudo yum install -y mysql-devel on the instance #
#######################################################


def create_app():
    application = Flask(__name__)
    FontAwesome(application)
    application.config['SECRET_KEY'] = 'Corallivore33' #need for search

    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    
    return application

application = create_app()
mysql = MySQL(application)


# class QueryForm(FlaskForm):
#     submit = SubmitField()

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
    # call cursor function to interact with db
    cursor=createCursor()

    # create variables for each search option
    params = request.form.get('search')
    tqry = request.form.get('onlyterms')
    dqry= request.form.get('onlydefs')
    nomatch = f"No results for {params} found"

    # perform search according to options
    if request.method == "POST":
        
        # if only searching terms
        if tqry != None:
            qry = params.title()
            qry=f"{params}%"
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s",(qry))
            results=cursor.fetchall()

        # if only searching definitions
        elif dqry != None:
            qry=f"%{params}%"
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Definition LIKE %s ",(qry))
            results=cursor.fetchall()

        # if both definitions and terms
        elif tqry != None and dqry != None:
            qry=f"%{params}%"
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s AND WHERE Definition LIKE %s ",(qry,qry))
            results=cursor.fetchall()

         # search all
        else:
            qry=f"%{params}%"
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s OR Definition LIKE %s OR Type LIKE %s",(qry,qry,qry))
            results=cursor.fetchall()

            
        return render_template('searchpage.html', results=results, nomatch=nomatch)
        
    return render_template('searchpage.html')


# define action for contributor page
@application.route('/contributors')
def contributors():
    return render_template('contributors.html')

# define action for about page
@application.route('/about')
def about():
    return render_template('aboutme.html')


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