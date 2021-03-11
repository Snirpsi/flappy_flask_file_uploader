import json, os, sys
from pprint import pprint
from attrdict import AttrDict, AttrMap
from types import SimpleNamespace

def convertDictToObject( convDict ):
    ret = empty()
    if (isinstance(convDict,dict)):
        for key in convDict.keys():
            setattr(ret,key,convertDictToObject(convDict[key]))
        return ret
    if (isinstance(convDict,list)):
        items = []
        for elem in convDict:
            items.append(convertDictToObject(elem))
        return items
    else:
        return  convDict



class empty:
    def __init__(self):
        pass

class CustomisationLoader:
    def __init__(self):
        with open("app/config.json") as json_file:
            json_data = json.load(json_file)
            useTexts = "default"
            if (os.getenv('CONF_FIELD')):
                useTexts = os.getenv('CONF_FIELD')
            json_data = json_data[useTexts] #select the configuration file
           
            self.conf = convertDictToObject(json_data)


