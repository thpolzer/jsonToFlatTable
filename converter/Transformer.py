import json


def getData(path):
    with open(path) as jsondata:
        return json.load(jsondata)


data = getData("/home/ubuntu/PycharmProjects/jsonToFlatTable/resources/jsontest.json")["root"]
print(data)


print(len(data[0]))


def flatten(jsondata,pairs,fathernode):
    for kvp in jsondata.items():
        if type(kvp[1]) is not dict and type(kvp[1]) is not list:
            if fathernode is None:
                pairs.append({kvp[0]:kvp[1]})
            else:
                pairs.append({fathernode+"."+kvp[0]: kvp[1]})
        elif type(kvp[1]) is dict:
                flatten(kvp[1],pairs,kvp[0])
        elif type(kvp[1]) is list:
            for item in kvp[1]:
                flatten(item,pairs,kvp[0])
    return pairs

def flatten_update(jsondata,pairs,fathernode):
    for kvp in jsondata.items():
        if type(kvp[1]) is not dict and type(kvp[1]) is not list:
            if fathernode is None:
                pairs.append({kvp[0]:kvp[1]})
            else:
                pairs.append({fathernode+"."+kvp[0]: kvp[1]})
        elif type(kvp[1]) is dict:
                flatten(kvp[1],pairs,kvp[0])
        elif type(kvp[1]) is list:
            for item in kvp[1]:
                flatten(item,pairs,kvp[0])
    return pairs



test = {"name":"Karl","amount":{"id":1,"name":"Anton"}}

pairs = []
result = flatten(data[0],pairs,None)

b = {"a":1}
b.update({"b":2})
b.update({"b":3})
a = 1
