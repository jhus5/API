import pymongo
from pymongo import MongoClient
from pymongo import collection

#extract metadata
#import subprocess


cluster = MongoClient("mongodb+srv://api:apipassword@metadata.tqne0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["metadata"]
collection = db["file_metadata"]

#post = {"customer": "mechmo", "hobbies": "crypto", "size":"xxxl", "diet": "strict-keto"} #metaadata extracted from files
post = {'ExifTool Version Number': '10.80', 'File Name': 'groot.jpg', 'Directory': '/content', 'File Size': '25 kB', 'File Modification Date/Time': '2021:12:29 13:02:46+00:00', 'File Access Date/Time': '2021:12:29 13:03:00+00:00', 'File Inode Change Date/Time': '2021:12:29 13:02:46+00:00', 'File Permissions': 'rw-r--r--', 'File Type': 'JPEG', 'File Type Extension': 'jpg', 'MIME Type': 'image/jpeg', 'JFIF Version': '1.01', 'Resolution Unit': 'inches', 'X Resolution': '72', 'Y Resolution': '72', 'Image Width': '356', 'Image Height': '500', 'Encoding Process': 'Progressive DCT, Huffman coding', 'Bits Per Sample': '8', 'Color Components': '3', 'Y Cb Cr Sub Sampling': 'YCbCr4:2:0 (2 2)', 'Image Size': '356x500', 'Megapixels': '0.178'}

#post
collection.insert_one(post)

#get by key

#get by key value