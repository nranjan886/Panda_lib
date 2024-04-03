from http import client
from urllib import request

import config.MongoConfig
import pandas as pd

from flask import Blueprint, request

import constants.MongoConstants

PANDA_LIB = Blueprint("PANDA_LIB", __name__)

@PANDA_LIB.route("/upload", methods=['POST'])
def upload_file():
    try:
        file = request.files.get("file")
        if file is None:
            return "No file uploaded", 400
        df = pd.read_excel(file)
        json_data = df.to_json(orient='records')

        conn = config.MongoConfig.get_connect()
        db = conn['my_db']
        collection = db["my_collection"]
        collection.insert_many[json_data]
        client.close()
        return "Data Updated successfully in mongoDB!!!"
    except Exception as e:
        print(e)


