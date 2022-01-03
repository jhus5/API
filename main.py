#import fastapi
from fastapi import FastAPI, File, UploadFile
from bson.objectid import ObjectId
#pymongo to communicate with MongoDB
import pymongo
from pymongo import MongoClient
from pymongo import collection
#import other
import subprocess
import shutil

#mongodb code
cluster = MongoClient("mongodb+srv://api:apipassword@metadata.tqne0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["metadata"]
collection = db["file_metadata"] #db.file_metadata

#fastapi app
app = FastAPI()


@app.get("/") #obtain status of server
async def root():
    return {"status": "running"}

@app.post("/extract-metadata")
async def create_upload_file(file: UploadFile = File(...)):
    #post metadata extracted from files
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
    
    #mongodb pipeline
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
    #mongodb pipeline
    pipeline = [
        {
            '$match': {
                '_id': ObjectId(extracted_id) 
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

  
@app.get("/query-metadata/")
async def query(tag: str = None, value: str = None): 
    #"query-metadata?tag=<tag>&value=<value>"
    #mongodb pipeline
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


        
@app.get("/get-all/") #retreiving all records
async def getAll():
    #mongodb pipeline
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