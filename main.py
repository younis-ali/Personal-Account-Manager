import sqlite3
import csv
from fastapi import FastAPI
import time


conn = sqlite3.connect('test.db')  # Connect to the database by conn object
def createDatabase():
  # This function connects to the database and creates the Expenses table
  print("Opened database successfully");

  conn.execute('''
  CREATE TABLE IF NOT EXISTS Expenses(Expense Type, 
                        Cost float, 
                        Date date);''')

  conn.commit()

  print("Table created successfully");

def enterData(query):
  createDatabase() 
  conn.execute(query)
  conn.commit()

def queries(auery):
  # This function implements the DML queries
  cursor = conn.execute(query)
  # open the file in the write mode
  f = open('data.csv', 'w')
  # create the csv writer
  writer = csv.writer(f)
  for row in cursor:
    print(row)
    # write a row to the csv file
    writer.writerow(row)

app = FastAPI()

@app.get('/')
async def root():
    return {'Assignment': 'Personal Accounts Manager'}

@app.post('/Enter Data into the table')
async def createTable(query: str):
  st = time.time()
  enterData(query)
  time_taken = time.time()-st
  return {'Info': 'Record Insterted successfully!', 'EXECUTION_TIME':'{:.2f}s'.format(time_taken)}

@app.post('/View data by entering DML Queries')
async def maniupulateData(query: str):
  st = time.time()
  queries(query)
  time_taken = time.time()-st
  return {'Info': 'Query executed successfully!', 'EXECUTION_TIME':'{:.2f}s'.format(time_taken)}