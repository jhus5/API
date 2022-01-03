# api_client_bw
 api - to store and query metadata extracted from files

# Requirements
The requirements.txt file lists everything that you need to run the app. These are:
	
* python
* bb
* ss
* ss
* ss
* ss

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


# Sample unit data file to test app
* unit_data https://github.com/Birkbeck/msc-information-technology-project-2020_21---files-jhussa09/tree/main/Unit_Data
