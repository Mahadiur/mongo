from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
import pprint
load_dotenv(find_dotenv())


# Cluster password
passward = os.environ.get('MONGODB_PWD')
# Connection url
connection_url = f'mongodb+srv://Mahadiur:{passward}@mongodbpractise.ywrnzxa.mongodb.net/'
# called this url
client = MongoClient(connection_url)

data = client.list_database_names()
testdata = client['TestDataBase01']
collection = testdata.list_collection_names()
# Define a function for insert data

def inserted_test_data():
    testcollection = testdata.TestDataBase01

    key_pair_data01 = {
        'Name' : 'Mahadi',
        'Designation': 'Ml Expert',
        'Salary': 200000
    }

    insert_ID = testcollection.insert_one(key_pair_data01).inserted_id
    print(f'Inserted ID: {insert_ID}')

inserted_test_data()