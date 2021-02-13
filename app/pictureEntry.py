#coding:utf8
import os, json
from markupsafe import escape
from datetime import datetime
from werkzeug.utils import secure_filename
import secrets
from app import app

path =  app.config['UPLOADED_IMAGES_DEST']
metaFileName = "metadata" 
alphabeth = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #must be url save and path save




class EntryMetadata:
    id=None
    email=None
    name=None
    aufnahmedatum=None
    uploadeDate=None
    beschreibung = None
    image = None
    filename = None
    fileextension = None



    def __init__(self,email=None,name=None,aufnahmedatum=None,beschreibung=None,image=None):
        
        if(image == None):
            return
    
        self.id = ''.join(secrets.choice(alphabeth) for i in range(20))#random id + location to save
        self.email= escape(email) 
        self.name=escape(name) 
        self.aufnahmedatum=escape(aufnahmedatum)
        self.beschreibung = escape(beschreibung)
        self.image = image
        self.filename = secure_filename(image.filename)
        self.fileextension =    self.filename.split('.')[-1]

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.uploadeDate = dt_string



    #saves image and metadata in folder with id name
    def save(self):
        os.mkdir(path + str(self.id),0o755)
        '''
        except OSError as e:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        '''
        #image saved first
        self.image.save(os.path.join(path, str(self.id) , "image" + "." + str(self.fileextension)  ))

        self.image = None#dont save image in json

        jsonStr = json.dumps(self.__dict__)
        print(jsonStr)
        fname = path + str(self.id) + "/" + str(metaFileName) + ".json"

        print(fname)

        f = open(fname, "w+")
        f.write(jsonStr)
        f.close()
    

#loades all entrys from file system
class EntryMetadataLoader:
    

    def __init__(self):
        pass
       
    #returns list of entrys in all data directories
    def loadeAll(self):
        data = []
        
        allids = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
        json_files =[] #Pfade der json metadaten files
    
        for index, id in enumerate(allids):
            print(id)

            json_files.insert(0, path + str(id) +"/" +[meta_json for meta_json in os.listdir( os.path.join(path, str(id) ) )if meta_json.endswith('.json')] [0] )
            print(json_files)

        for index, js in enumerate(json_files):
            print(js)
            with open(os.path.join( js)) as json_file:
                json_string = json.load(json_file)
                
                print(json_string["email"])
                entry = EntryMetadata()
                entry.id = json_string["id"]
                entry.email= json_string["email"]
                entry.name = json_string["name"]
                entry.aufnahmedatum=json_string["aufnahmedatum"]
                entry.beschreibung = json_string["beschreibung"]
                entry.image = None ## dont loade image here
                entry.filename = json_string["filename"]
                entry.fileextension =  json_string["fileextension"]
                entry.uploadeDate= json_string["uploadeDate"]

                data.insert(0,entry)
        return data