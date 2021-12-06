# Personal-Account-Manager
''' This project is the demo of Personal Account Manager.
we use sqlite package of python to create the database. To interact with
the database tables we use FastAPI where we can type queries to insert records 
into the table and DML queries also. After executing DML queries the output is
stored in csv file '''

I run the program in google colab and the notebook is also in the repository. 

Requirements
1. Uvicorn server
2. FastAPI
3. sqllite

USAGE
1. Install the requirements.
2. uvicorn main:app --reload
  INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
3. Then open the url in browser and append /docs for GUI "http://127.0.0.1:8000/docs"
  
