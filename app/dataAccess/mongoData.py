from bson.objectid import ObjectId
from flask_pymongo import PyMongo

mongo = None


class mongoData:

    # constructor
    def __init__(self, app):
        self.app = app

    def __get_mongo(self):
        global mongo

        if 'MONGO_URI' not in self.app.config:
            self.app.config['MONGO_URI'] = os.getenv(
                'MONGO', 'mongodb://localhost:27017/pk_7in14')

        if not mongo:
            mongo = PyMongo(self.app)

        return mongo

    def get_all(self):
        return self.__get_mongo().db.dataSources.find({})

    def add_one(self, data):
        return self.__get_mongo().db.dataSources.insert_one(data)

    def remove_one(self, id):
        return self.__get_mongo().db.dataSources.delete_one({'_id': ObjectId(id)})

    def get_one(self, id):
        return self.__get_mongo().db.dataSources.find_one_or_404(ObjectId(id))
