# Module imports

from flask import Flask, render_template, url_for, redirect, request 
#from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from flask_mysqldb import MySQL 
import pymysql
import pymysql.cursors

# Imports from other files
# from forms import sitesearch


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

# connect with pymysql - config
conf = {
    "host": 'coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com',
    "port": 3306,
    "user": "master",
    "password": "CoralWiki2021",
    "cursorclass": pymysql.cursors.DictCursor,
    "database": "CCRW"
}

# # for local testing
# conf = {
#     "host": 'localhost',
#     "unix_socket": '/tmp/mysql.sock',
#     "user": "amanda",
#     "password": '',
#     "cursorclass": pymysql.cursors.DictCursor,
#     "database": "CCRW"
# }

class QueryForm(FlaskForm):
    submit = SubmitField()

# use pymysql cursor to interact with MySQL database
def createCursor():
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    return cursor


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
    cursor=createCursor()

    # params = request.form['search']
    # tqry = request.form['onlyterms']
    # dqry= request.form['onlydefs']
    params = request.form.get('search')
    tqry = request.form.get('onlyterms')
    dqry= request.form.get('onlydefs')
    nomatch = f"No results for {params} found"
    if request.method == "POST":
        print(params,tqry,dqry)
        
        # if only searching terms
        if tqry != None:
            qry=f"%{params}%"
            print(qry)
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s",(qry))
            results=cursor.fetchall()
            print(len(results))
        # if only searching definitions
        elif dqry != None:
            qry=f"%{params}%"
            print(qry)
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Definition LIKE %s ",(qry))
            results=cursor.fetchall()
            print(len(results))
        elif tqry != None and dqry != None:
            qry=f"%{params}%"
            print(qry)
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s AND WHERE Definition LIKE %s ",(qry,qry))
            results=cursor.fetchall()
            print(len(results))
        else:
            # search all
            qry=f"%{params}%"
            print(qry)
            cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions WHERE Term LIKE %s OR Definition LIKE %s OR Type LIKE %s",(qry,qry,qry))
            results=cursor.fetchall()
            print(len(results))

        # for i in results:
        #         print(i)
                # term = i['Term']
                # type = i['Type']
                # defin = i['Definition']
            
        return render_template('searchpage.html', results=results, nomatch=nomatch)
        
    return render_template('searchpage.html')

   

# @application.route('/results', methods=['POST'])
# def search_results():
# # set up cursor to search db
#     # conn = pymysql.connect(**conf)
#     # cursor = conn.cursor()

#     # if request.method == 'POST':
#     #     qry = request.form['search']
        
#     #     details = cursor.get_details()
#     #     print(details)
#     #     for detail in details:
#     #         results = detail

#     return render_template('results.html')


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