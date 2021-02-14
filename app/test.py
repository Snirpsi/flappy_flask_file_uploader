
class empty:
    def __init__(self):
        pass

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", {"band":"ACDC","loft":123 } , "white", "blue"]
}

def convertDictToObject( convDict ):
    ret = empty()
    if (isinstance(convDict,dict)):
        for key in convDict.keys():
            print(key)
            setattr(ret,key,convertDictToObject(convDict[key]))
        return ret
    if (isinstance(convDict,list)):
        items = []
        for elem in convDict:
            items.append(convertDictToObject(elem))
        return items
    else:
        return  convDict


print( thisdict )
print( thisdict.keys() )

print(convertDictToObject( thisdict ).colors[1].band)