# Configurations for using PyMySQL to connect to MySQL db
# Coral db at coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com or ip-10-20-0-201
# the schema(db) is CCRW
    
import pymysql.cursors

url =  'coral-wiki.cgt5nl4ooura.us-east-2.rds.amazonaws.com'

conf = {
    "host": url,
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
