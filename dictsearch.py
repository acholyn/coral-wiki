from application import createCursor
from flask import request 


def searchdict(params,tqry,dqry):

    # call cursor function to interact with db
    cursor=createCursor()

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
        print(qry,results)

        return results