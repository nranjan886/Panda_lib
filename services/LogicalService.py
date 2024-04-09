from config.MongoConfig import get_connect
import pandas as pd
def addAndUpdate(data):
    try:
        conn = get_connect()
        db = conn['my_db']
        collection = db["my_sum"]
        columns = ['_id', 'x', 'y']
        df = pd.DataFrame(data, columns=columns)

        if '_id' in df.columns:
            df.drop(columns=['_id'], inplace=True)

        df["z"] = df["x"] + df["y"]
        json_data = df.to_dict(orient='records')
        collection.insert_many(json_data)
        conn.close()
        print("Data updated successfully in MongoDB!!!")
    except Exception as e:
        print(e)



