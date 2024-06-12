import pymongo

from pymongo import MongoClient

connection=MongoClient('localhost',27017)

db=connection['details']

collection=db['language']

document={'title':'HTML','type':'Markup Language','use':'Web App'}

result=collection.insert_one(document)

print(f"Inserted document ID: {result.inserted_id}")