# imports for online file reading
import csv
import urllib.request
import shutil
import tempfile

import pandas
from flask import Flask, redirect, render_template, request, url_for
#from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_wtf import FlaskForm
# imports for search
from wtforms import Form, SelectField, StringField, SubmitField


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

# #searchform actions
#     class searchform(Form):
#         choices = [('term', 'term'),
#                 ('type', 'type'),
#                 ('description', 'description')]
#         select = SelectField('search:', choices=choices)
#         search = StringField('')

#     # search = searchform(request.form)
#     # if request.method == 'post':
#     #         return search_results(search)

#     results = []
#     search_string = search.data['search']

# definitions

    with urllib.request.urlopen('https://docs.google.com/spreadsheets/d/e/2PACX-1vS8dVMITvA6q77MTBe4SShI9Q85G4A_3Y5C8xx7n-BLinoxOW0y7zI59qoLxgwQ0Aql-I_MBye1UY6G/pub?gid=0&single=true&output=tsv') as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    with open(tmp_file.name) as file:
        coraldefs=pandas.read_csv(file, sep="\t", keep_default_na=False)
        term=coraldefs.TERM
        role=coraldefs.ROLE 
        definition=coraldefs.DEFINITION 
        referrals=coraldefs.REFERRALS
        length=len(coraldefs)
        print(length)


    return render_template('index.html', coraldefs=coraldefs, term=term, role=role, definition=definition, referrals=referrals)



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
