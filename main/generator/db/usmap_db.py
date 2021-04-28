""" This file is used to put the state_google.csv into vaccine db"""
import sqlite3
import pandas as pd

connection = sqlite3.connect('Vaccine.db')
df = pd.read_csv('state_google.csv')
df.to_sql('state_google', connection, if_exists='append', index=False)
cursor = connection.cursor()
cursor.execute("select state from state_google ")

print (cursor.fetchall())
connection.commit()
connection.close()
