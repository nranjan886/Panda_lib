from urllib import request
import config.MongoConfig
import pandas as pd

from flask import Blueprint, request, jsonify

from services.LogicalService import addAndUpdate
from services.MongoRepo import findAll

PANDA_LIB = Blueprint("PANDA_LIB", __name__)

@PANDA_LIB.route("/upload", methods=['POST'])
def upload_file():
    try:
        file = request.files.get("data")
        if file is None:
            return "No file uploaded", 400
        df = pd.read_excel(file)
        json_data = df.to_dict(orient='records')

        conn = config.MongoConfig.get_connect()
        db = conn['my_db']
        collection = db["my_collection"]
        collection.insert_many(json_data)
        conn.close()
        return "Data Uploaded successfully to MongoDB!!!", 200
    except Exception as e:
        print(e)
        return "An error occurred while processing the file", 500

@PANDA_LIB.route("/read-data", methods=['GET'])
def read_data():
    try:
        conn = config.MongoConfig.get_connect()
        db = conn['my_db']
        collection = db["my_collection"]
        data = list(collection.find({}))  # Fetch all documents from the collection
        conn.close()

        df = pd.DataFrame(data)
        if '_id' in df.columns:
            df.drop('_id', axis=1, inplace=True)

        return df.to_json(orient='records'), 200
    except Exception as e:
        print(e)
        return "An error occurred while retrieving data", 500

@PANDA_LIB.route("/calculate-sum", methods=['GET'])
def calculate_sum():
    try:
        data = findAll()
        # Assuming addAndUpdate() calculates sum of 'x' and 'y' and updates data with the result
        addAndUpdate(data)
        print("Sum of x and y stored in MongoDB as z for each document.")
        return "Sum calculated and stored successfully", 200  # Add return statement here
    except Exception as e:
        print(e)
        return "An error occurred while calculating and storing the sum", 500




