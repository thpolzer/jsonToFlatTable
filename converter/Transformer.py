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

def flatten_update(jsondata,pairs,fathernode,level):
    for kvp in jsondata.items():
        if type(kvp[1]) is not dict and type(kvp[1]) is not list:
            if fathernode is None:
                pairs.append({kvp[0]+"."+str(level):kvp[1]})
            else:
                pairs.append({fathernode+"."+kvp[0]+"."+str(level): kvp[1]})
        elif type(kvp[1]) is dict:
                flatten_update(kvp[1],pairs,kvp[0]+"."+str(level),0)
        elif type(kvp[1]) is list:
            i = 0
            for item in kvp[1]:
                flatten_update(item,pairs,kvp[0]+"."+str(level),i)
                i += 1
    return pairs


def flatten_update1(jsondata,d,fathernode,level):
    for kvp in jsondata.items():
        if type(kvp[1]) is not dict and type(kvp[1]) is not list:
            if fathernode is None:
                d.update({kvp[0]+"."+str(level):kvp[1]})
            else:
                d.update({fathernode+"."+kvp[0]+"."+str(level): kvp[1]})
        elif type(kvp[1]) is dict:
                flatten_update1(kvp[1],d,kvp[0]+"."+str(level),0)
        elif type(kvp[1]) is list:
            i = 0
            for item in kvp[1]:
                flatten_update1(item,d,kvp[0]+"."+str(level),i)
                i += 1
    return d



test = {"name":"Karl","amount":{"id":1,"name":"Anton"}}

pairs = []
d = {}
#result = flatten(data[0],pairs,None)
#result = flatten_update(data[0],pairs,None,0)
result1 = flatten_update1(data[0],d,None,0)

b = {"a":1}
b.update({"b":2})
b.update({"b":3})
a = 1
