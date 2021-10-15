from flask import Flask, render_template, url_for, redirect, request 
# from flask_sqlalchemy import SQLAlchemy
#from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_mysqldb import MySQL 
# import MySQLdb.connections
import MySQLdb.cursors
import mysql.connector


#######################################################
# run sudo yum install -y mysql-devel on the instance #
#######################################################

def create_app():
    application = Flask(__name__)
    FontAwesome(application)
    application.config['SECRET_KEY'] = 'change this unsecure key' #need for search
    application.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    # Coral db at coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com or ip-10-20-0-201
    # db connection configuration, the schema(db) is CCRW

    # # for local testing: amanda@localhost::/tmp/mysql.sock
    # application.config['MYSQL_DATABASE_HOST'] = 'localhost'
    # application.config['MYSQL_UNIX_SOCKET'] = '/tmp/mysql.sock'
    # application.config['MYSQL_DATABASE_USER'] = 'amanda'
    # application.config['MYSQL_DATABASE_PASSWORD'] = ''
    # application.config['MYSQL_DB'] = 'CCRW'
    
    application.config['MYSQL_DATABASE_HOST'] = 'coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com'
    application.config['MYSQL_DATABASE_PORT'] = '3306'
    application.config['MYSQL_DATABASE_USER'] = 'master'
    application.config['MYSQL_DATABASE_PASSWORD'] = 'CoralWiki2021'
    application.config['MYSQL_DATABASE_DB'] = 'CCRW'
    
    return application

application = create_app()
mysql = MySQL(application)
# mysql.init_app(application)



# define actions for home page
@application.route('/')
def index():

    #Creating a connection cursor to interact with the tables
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cnx = mysql.connector.connect(user='master', password='CoralWiki2021', host='coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com', port='3306', database='CCRW')
    cursor = cnx.cursor()
   
    # defsdata=cursor.execute('SELECT Term,Type,Definition,Referrals FROM CCRW.CoralDefinitions' )
    cursor.execute("SELECT * FROM CCRW.CoralDefinitions")
    defsdata = cursor.fetchall()

    return render_template('index.html', defsdata=defsdata)

# define action for contributor page
@application.route('/contributors')
def contributors():
    return render_template('contributors.html')

# define action for about page
@application.route('/about')
def about():
    return render_template('about.html')


# No caching at all for API endpoints.
@application.after_request
def add_header(response):
    # response.cache_control.no_store = True
    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == "__main__":
    application.run(debug=True)

    # export FLASK_APP=application.py