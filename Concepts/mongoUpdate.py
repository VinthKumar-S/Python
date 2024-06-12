import pymongo

from pymongo import MongoClient

connection=MongoClient('localhost',27017)

db=connection['details']

collection=db['language']

get_title=input('Language:')

title={'title':get_title}

result=collection.find(title)

print('previous:')
for document in result:
    print(document)


get_selectedTitle=input('title:')

get_value=input('value:')

selectedTitle={'title':get_title}

update_data={'$set':{get_selectedTitle:get_value}}

result_update=collection.update_one(selectedTitle,update_data)

result_final=collection.find(title)

print('now:')
for document in result_final:
    print(document)

connection.close()