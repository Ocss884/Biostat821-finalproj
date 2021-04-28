"""Create vaccine database and insert pfizer and moderna vaccine data into the db"""
import sqlite3
from time import sleep
#import uuid
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import urllib.request
import json

APP = FastAPI()

connection = sqlite3.connect("Vaccine.db")
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Moderna_allocation( 
    Jurisdiction          VARCHAR (255),
    Week_of_allocation      VARCHAR2 (255),
    first_dose_allocation   Numeric (20),
    second_dose_allocation  Numeric(20)
    )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Pfizer_allocation( 
    Jurisdiction          VARCHAR (255),
    Week_of_allocation      VARCHAR2 (255),
    first_dose_allocation   Numeric (20),
    second_dose_allocation  Numeric(20)
    )''')
connection.commit()
connection.close()
class URL(BaseModel):
    url: str

@APP.get("/")
def handle_slash():
    """Handle root."""
    return "Hello world!"
    
@APP.post("/Moderna_allocation")
def load_Moderna_allocation(link:URL):
    try:
        resp = urllib.request.urlopen(link.url)
        ele_json = json.loads(resp.read())
    except IOError:
        raise "Cannot find the files or the fail to read the file!"
    admin =[]
    for idx in ele_json:
        idx['week_of_allocations'] = idx['week_of_allocations'][0:10]
        admin.append(list(idx.values()))

    connection = sqlite3.connect("Vaccine.db")
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO Moderna_allocation VALUES (?, ?, ?,?)', admin)
    connection.commit()
    connection.close()
    return "Create Successfully"

@APP.post("/Pfizer_allocation")
def load_Pfizer_allocation(link:URL):
    try:
        resp = urllib.request.urlopen(link.url)
        ele_json = json.loads(resp.read())
    except IOError:
        raise "Cannot find the files or the fail to read the file!"
    admin =[]
    for idx in ele_json:
        idx['week_of_allocations'] = idx['week_of_allocations'][0:10]
        admin.append(list(idx.values()))

    connection = sqlite3.connect("Vaccine.db")
    cursor = connection.cursor()
    cursor.executemany('INSERT INTO Pfizer_allocation VALUES (?, ?, ?,?)', admin)
    connection.commit()
    connection.close()
    return "Create Successfully"


