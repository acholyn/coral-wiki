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



# define actions for home page
@application.route('/', methods=['GET', 'POST'])
def index():

    # use pymysql cursor to interact with MySQL database
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    defsdata=cursor.execute("SELECT * FROM CoralDefinitions")
    defsdata = cursor.fetchall() # makes selection iterable

    return render_template('index.html', defsdata=defsdata, )


# actions for search page
@application.route('/search', methods=['GET', 'POST'])
def search():
    # set up cursor to search db
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()

    if request.method == "POST":
        search = request.form['search']

        # search by all fields except referrals
        cursor.execute('''SELECT Term, Type, Definition, Referrals FROM CoralDefinitions WHERE Term LIKE %s OR Type LIKE %s OR Definition LIKE %s ''', (search, search, search))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        # if len(data) == 0 and search == 'all': 
        #     cursor.execute("SELECT Term, Type, Definition FROM CoralDefinitions")
        #     conn.commit()
        #     data = cursor.fetchall()
        return render_template('searchpage.html', data=data)


# @application.route('/results')
# def search_results(search,**args):

#     # use pymysql cursor to interact with MySQL database
#     conn = pymysql.connect(**conf)
#     cursor = conn.cursor()
#     searchqry=cursor.execute("SELECT * FROM CoralDefinitions WHERE %s LIKE %s " % (search))
#     results = list(searchqry.fetchall())
    
#     for r in results:
#         print(f"{r.Term} ({r.Type}): {r.Definition}")
#     # search_string = search.data['search']
#     # if search.data['search'] == '':

#     #     qry = db_session.query(Album)
#     #     results = qry.all()
#     # # if not results:
#     # #     flash('No results found!')
#     # #     return redirect('/')
#     # else:
#         # display results
#     return render_template('results.html', results=results)

def get_details():
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM CoralDefinitions''') 
    # WHERE Term LIKE %s OR Type LIKE %s OR Definition LIKE %s ''', (qry, qry, qry))
    details = cursor.fetchall()
    return details

@application.route('/results', methods=['POST'])
def search_results(search,**args):
# set up cursor to search db
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()

    if request.method == 'POST':
        qry = request.form['search']
        
        details = cursor.get_details()
        print(details)
        for detail in details:
            results = detail
    return render_template('results.html', results=results)


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