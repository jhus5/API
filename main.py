from bson.objectid import ObjectId
from fastapi import FastAPI, File, UploadFile

#
import pymongo
from pymongo import MongoClient
from pymongo import collection

#import 
import subprocess
import shutil
from bson.objectid import ObjectId

#mongodb code
cluster = MongoClient("mongodb+srv://api:apipassword@metadata.tqne0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["metadata"]
collection = db["file_metadata"] #db.file_metadata

#
app = FastAPI()


@app.get("/") #obtain status of server
async def root():
    return {"status": "running"}

@app.post("/extract-metadata")
async def create_upload_file(file: UploadFile = File(...)):
    #post #metadata extracted from files
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    p1 = subprocess.run(['exiftool', file.filename], capture_output=True, check=True, universal_newlines=True) #capturing out to a variable

    metadata = [] #list to store metadata
    metadict = {} #dictionary to store file metadata

    #creating key value pairs from metadata
    line1 = p1.stdout.replace("  ", "").split("\n")
    for element in line1:
        if element == '': #loop to remove empty elements
            continue
        else:
            info = {} #dictionary to store key value pairs
            line2 = element.split(":", 1)
            info[line2[0].strip()] = line2[1].strip()
            metadata.append(info)
            metadict.update(info)

    file = collection.insert_one(metadict)
    
    pipeline = [
        {
            '$match': {
                '_id': ObjectId(file.inserted_id)
            }
        }, {
            '$project': {
                'Extraction id': {
                    '$toString': '$_id'
                }, 
                'File Path': {
                    '$toString': '$_Directory'
                }, 
                '_id': 0, 
                'File Name': 1, 
                'MIME Type': 1, 
                'File Type Extension': 1, 
                'File Path': 1, 
                'Modify Date': 1, 
                'File Modification Date/Time': 1
            }
        }
    ]
    
    list = []
    for doc in collection.aggregate(pipeline):
        list.append(doc)    
    return list
   

@app.get("/get-metadata/") #path parameter
# The web framework gets post_id from the URL and passes it as a string
async def get_by_id(extracted_id: str):
    pipeline = [
        {
            '$match': {
                '_id': ObjectId(extracted_id) #test '61d0f096a6cc29921c17d76a'
            }
        }, {
            '$project': {
                'Extraction id': {
                    '$toString': '$_id'
                }, 
                'File Path': {
                    '$toString': '$_Directory'
                }, 
                '_id': 0, 
                'File Name': 1, 
                'MIME Type': 1, 
                'File Type Extension': 1, 
                'File Path': 1, 
                'Modify Date': 1, 
                'File Modification Date/Time': 1
            }
        }
    ]
    
    list = []
    for doc in collection.aggregate(pipeline):
        list.append(doc)    
    return list

    #response = collection.aggregate(pipeline)
    #return = response

  
@app.get("/query-metadata/") #{tag}/{value}") #query parameter
async def query(tag: str = None, value: str = None): #'*, post_id: str = None,'
    #"query-metadata?tag=<tag>&value=<value>"
    
    pipeline = [
        {
            '$match': {
                tag: value
            }
        }, {
            '$project': {
                'Extraction id': {
                    '$toString': '$_id'
                }, 
                'File Path': {
                    '$toString': '$_Directory'
                }, 
                '_id': 0, 
                'File Name': 1, 
                'MIME Type': 1, 
                'File Type Extension': 1, 
                'File Path': 1, 
                'Modify Date': 1, 
                'File Modification Date/Time': 1
            }
        }
    ]
    
    list = []
    for doc in collection.aggregate(pipeline):
        list.append(doc)    
    return list


        
@app.get("/get-all/") #path parameter
# The web framework gets post_id from the URL and passes it as a string
async def getAll():
    # retreiving all records
    pipeline =  [
        {
            '$project': {
                'Extraction id': {
                    '$toString': '$_id'
                }, 
                'File Path': {
                    '$toString': '$_Directory'
                }, 
                '_id': 0, 
                'File Name': 1, 
                'MIME Type': 1, 
                'File Type Extension': 1, 
                'File Path': 1, 
                'Modify Date': 1, 
                'File Modification Date/Time': 1
            }
        }
    ]
    
    list = []
    for doc in collection.aggregate(pipeline):
        list.append(doc)    
    return list 