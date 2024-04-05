from urllib import request
import config.MongoConfig
import pandas as pd

from flask import Blueprint, request, jsonify

PANDA_LIB = Blueprint("PANDA_LIB", __name__)

@PANDA_LIB.route("/upload", methods=['POST'])
def upload_file():
    try:
        file = request.files.get("file")
        if file is None:
            return "No file uploaded", 400
        df = pd.read_excel(file)
        json_data = df.to_dict(orient='records')

        conn = config.MongoConfig.get_connect()
        db = conn['my_db']
        collection = db["my_collection"]
        collection.insert_many(json_data)
        conn.close()
        return "Data Updated successfully in mongoDB!!!"
    except Exception as e:
        print(e)


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
        return df.to_json(orient='records')
    except Exception as e:
        print(e)


