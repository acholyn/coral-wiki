# create pymysql cursor to interact with MySQL database
import pymysql
import pymysql.cursors
from sqlconf import conf # use config file


def createCursor():
    conn = pymysql.connect(**conf)
    cursor = conn.cursor()
    return cursor