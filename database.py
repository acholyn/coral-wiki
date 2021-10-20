# # this file is a stub; not sure if it works and wasn't used for the coral wiktionary


# # db_creator.py
# from application import db
# from sqlalchemy import create_engine, ForeignKey
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, backref, sessionmaker


# def Load_Data(file_name):
#     data = genfromtxt(file_name, delimiter='\t', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()

# Base = declarative_base()

# # outline table details for SQLAlchemy
# class dictionary(Base):
#     __tablename__ = "dictionary"

#     id = Column(Integer, primary_key=True)
#     term = Column(String, nullable=False)
#     role = Column(String, nullable=False)
#     definition = Column(Text, nullable=True)
#     referrals = Column(Text, nullable=True)


#     def __repr__(self):
#         return "{}".format(self.name)



# # create tables
# if __name__ == "__main__":

#     engine = create_engine('sqlite:///coraldefs.db', echo=True)
#     Base.metadata.create_all(engine)

#     #Create the session
#     session = sessionmaker()
#     session.configure(bind=engine)
#     s = session()

#     try:
#         file_name = "/Users/amanda/Desktop/coral/coraldefs.coraldefs.tsv" #sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
#         data = Load_Data(file_name) 

#         for i in data:
#             record = dictionary(**{
#                 'ID' :i[0],
#                 'TERM' : i[1],
#                 'ROLE' : i[2],
#                 'DEFINITION' : i[3],
#                 'REFERRALS' : i[4],
#             })
#             s.add(record) #Add all the records

#         s.commit() #Attempt to commit all the records
#     except:
#         s.rollback() #Rollback the changes on error
#     finally:
#         s.close() #Close the connection
#     #print "Time elapsed: " + str(time() - t) + " s." #0.091s
