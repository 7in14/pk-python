from bson.objectid import ObjectId


class mongoData:

    # constructor
    def __init__(self, mongo):
        self.mongo = mongo

    def get_all(self):
        return self.mongo.db.dataSources.find({})

    def add_one(self, data):
        return self.mongo.db.dataSources.insert_one(data)

    def remove_one(self, id):
        return self.mongo.db.dataSources.delete_one({'_id': ObjectId(id)})

    def get_one(self, id):
        return self.mongo.db.dataSources.find_one_or_404(ObjectId(id))
