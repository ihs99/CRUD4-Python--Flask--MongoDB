from pymongo import MongoClient
import certifi


MONGO_URI = 'mongodb+srv://user:password@cluster0.f5vxk.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error connecting to the ddbb')
    return db
