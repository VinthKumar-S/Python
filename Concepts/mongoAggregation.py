import pymongo

from pymongo import MongoClient

connection=MongoClient('localhost',27017)

db=connection['details']

collection=db['language']

pipline=[
    {"$limit":3},
]

query={'use':'Mobile'}

sortResult=collection.find(query).sort('title',-1)

print("Sort:")
for doc in sortResult:
    print(doc)
    print("")


print("Limit:")

result=collection.aggregate(pipline)

for document in result:
    print(document)
    print("")

connection.close()