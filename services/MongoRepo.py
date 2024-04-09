import config.MongoConfig

def findAll():
    conn = config.MongoConfig.get_connect()
    db = conn['my_db']
    collection = db["my_collection"]

    # Fetch data from the collection
    data = list(collection.find({}))
    return data