# api_client_bw
 api - to store and query metadata extracted from files

# Requirements
The requirements.txt file lists everything that you need to run the app. These are:
	
* python==3.8.1
* anyio==3.4.0
* asgiref==3.4.1
* click==8.0.3
* dnspython==2.1.0
* fastapi==0.70.1
* h11==0.12.0
* httptools==0.3.0
* idna==3.3
* pydantic==1.8.2
* pymongo==4.0.1
* python-dotenv==0.19.2
* python-multipart==0.0.5
* PyYAML==6.0
* six==1.16.0
* sniffio==1.2.0
* starlette==0.16.0
* typing-extensions==4.0.1
* uvicorn==0.16.0
* uvloop==0.16.0
* watchgod==0.7
* websockets==10.1

To install these requirements run the following command by saving the requirements.txt file and changing to the directory from a terminal window:
	
	pip install -r requirement.txt 
  
You will also need to install Exiftool by Phil Harvey

	http://web.mit.edu/graphics/src/Image-ExifTool-6.99/html/index.html 
 
For example, if you are running on Ubuntu then you can simply run the following command:

 	sudo apt install exiftool
 
# Running the app
To run the app you can use the following command from a terminal from the directory where 'main.py' is saved:

  	uvicorn main:app --reload

Now open a browser to:

  http://127.0.0.1:8000 

You should see a JSON response:

   	{"status":"running"}

# Interactive API documentation
FastAPI comes with API documentation courtesy of swagger ui. To access this you should naviagte to:

   http://127.0.0.1:8000/docs

# Access endpoints
You can access and test all the endpoints from the interactive api documentation as well as test it out.

# FastAPI
FastAPI was selected due to its high performance, especially with large amounts of data, and being fast to code. 

# Database
MongoDB has been selected to file metadata with data being stored in self-contained JSON like documents. Being a NoSQL database MongoDB is also scalable horizontally. Querying in MongoDB is fast and aggregation pipeline has been utlised for querying. Aggregation operations allow for operations to run on the server. With a a large number of file data MongoDb also offers index feature, which allows to querying through indexes in addition to primary keys. 
