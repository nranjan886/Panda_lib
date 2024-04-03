from pymongo import MongoClient, errors
from config.EnvConfig import get_env_config

conf = get_env_config()

def get_connect():
    try:
        conn = MongoClient("mongodb://localhost:27017/?directConnection=true", serverSelectionTimeoutMS=2000)
        conn.server_info()
        return conn
    except errors.ServerSelectionTimeoutError as err:
        print("connection error, check your connection string: " + str(err))
