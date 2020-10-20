import pymongo
import json
from bson import ObjectId
import datetime
from pymongo.errors import BulkWriteError

client = pymongo.MongoClient(host='127.0.0.1', port=27017)


class JSONEncoder(json.JSONEncoder):
    """ 处理ObjectId,该类型无法转为json """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return datetime.datetime.strftime(o, '%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, o)


class MongoModel(object):

    def __init__(self, *args, **kwargs):
        self.db = client.pipeline
        self.collection = None
        self.args = args
        self.kwargs = kwargs

    def update(self, term, data):
        return self.collection.update(term, {"$set": data}, True)

    def save(self):

        if len(self.args) > 0:
            res = []
            results = self.collection.insert_many(self.args)
            return json.loads(JSONEncoder().encode(results.inserted_ids))
            # for r in results:
            #     res.append(json.loads(JSONEncoder().encode(r)))
            # return res
        return self.collection.insert_one(self.kwargs)
        # return json.loads(JSONEncoder().encode(self.collection.insert_one(self.kwargs)))

    def get_one(self, params={}):
        try:
            return json.loads(JSONEncoder().encode(self.collection.find_one(params)))
        except:
            return None

    def get_all(self, params={}):
        res = []
        # print(params)
        for r in self.collection.find(params):
            res.append(json.loads(JSONEncoder().encode(r)))
        return res

    def getNextValue(self):
        ret = self.collection.find_and_modify({"_id": "auto_id"}, {"$inc": {"sequence_value": 1}}, safe=True, new=True)
        new = ret["sequence_value"]
        return new

    def delete(self, params):
        self.collection.delete_many(params)
        return


class Template(MongoModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = self.db.d_template


class Taskflow(MongoModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collection = self.db.d_Taskflow
