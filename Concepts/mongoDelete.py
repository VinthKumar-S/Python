import pymongo

from pymongo import MongoClient

connection=MongoClient('localhost',27017)

db=connection['details']

collection=db['language']

get_title=input('Language:')

title={'title':get_title}

result=collection.delete_one(title)

connection.close()