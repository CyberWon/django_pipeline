
from pymongo.collection import ObjectId
import json


def Q2D_POST(request):
    _data = {}
    try:
        d = json.loads(request.body)
        if isinstance(d, list):
            return d
        for key in d:
            if key == "_id":
                value = ObjectId(d[key])
                _data[key] = value
            else:
                _data[key] = d[key]
    except:
        d = request.POST.items()
        for key, value in d:
            if key == "_id":
                value = ObjectId(value)
            _data[key] = value
    return _data
