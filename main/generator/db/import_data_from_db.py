import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

""" Load the data from Vaccine database and trun them into dataframe so that the data can be used in further analysis"""
"""Create Moderna dataframe"""
connection = sqlite3.connect('Vaccine.db')
cursor = connection.cursor()
cursor.execute("select * from Moderna_allocation")
modernalist = cursor.fetchall()
#print(moderna)
Jurisdiction = []
Week_allocation = []
first_dose = []
second_dose = []
for idx in range(0, len(modernalist)):
    Jurisdiction.append(modernalist[idx][0])
for idx in range(0, len(modernalist)):
    Week_allocation.append(modernalist[idx][1])
for idx in range(0, len(modernalist)):
    first_dose.append(modernalist[idx][2])
for idx in range(0, len(modernalist)):
    second_dose.append(modernalist[idx][3])
moderna = pd.DataFrame({'Jurisdiction':Jurisdiction ,'Week of Allocations': Week_allocation,'1st Dose Allocations':first_dose,'2nd Dose Allocations':second_dose})

""" Create pfizer dataframe"""
cursor.execute("select * from Pfizer_allocation")
pfizerlist = cursor.fetchall()
#print(moderna)
Jurisdiction = []
Week_allocation = []
first_dose = []
second_dose = []
for idx in range(0, len(pfizerlist)):
    Jurisdiction.append(pfizerlist[idx][0])
for idx in range(0, len(pfizerlist)):
    Week_allocation.append(pfizerlist[idx][1])
for idx in range(0, len(pfizerlist)):
    first_dose.append(pfizerlist[idx][2])
for idx in range(0, len(pfizerlist)):
    second_dose.append(pfizerlist[idx][3])
pfizer = pd.DataFrame({'Jurisdiction':Jurisdiction ,'Week of Allocations': Week_allocation,'1st Dose Allocations':first_dose,'2nd Dose Allocations':second_dose})

""" Create US map dataframe"""
cursor.execute("select * from state_google")
usmaplist = cursor.fetchall()
States =[]
lat = []
lon = []
Jurisdiction = []
population = []
print(usmaplist)
for idx in range(0, len(usmaplist)):
    Jurisdiction.append(usmaplist[idx][3])
for idx in range(0, len(usmaplist)):
    States.append(usmaplist[idx][0])
for idx in range(0, len(usmaplist)):
    lat.append(usmaplist[idx][1])
for idx in range(0, len(usmaplist)):
    lon.append(usmaplist[idx][2])
for idx in range(0, len(usmaplist)):
    lon.append(usmaplist[idx][4])
usmap = pd.DataFrame({'States':States ,'lat': lat,'lon':lon,'Jurisdiction':Jurisdiction,'population':population})
print(usmap)

#usmap.columns = ["States", "lat", "lon", "Jurisdiction"]
pfizer["Week of Allocations"] = pd.to_datetime(pfizer["Week of Allocations"])
moderna["Week of Allocations"] = pd.to_datetime(moderna["Week of Allocations"])

pfizer_before = pfizer[
    (pfizer["Week of Allocations"] >= "2021-03-01")
    & (pfizer["Week of Allocations"] <= "2021-04-19")
]
pfizer_sorted = pfizer_before.sort_values(by = ["Week of Allocations"], ascending = True)
pfizer_sorted["Cumulative Allocations"] = pfizer_sorted.groupby(["Jurisdiction"])["1st Dose Allocations"].apply(lambda x: x.cumsum())
pfizer_data = pfizer_sorted.merge(usmap, how = "left", on = "Jurisdiction")

moderna_before = moderna[
    (moderna["Week of Allocations"] >= "2021-03-01")
    & (moderna["Week of Allocations"] <= "2021-04-19")
]
moderna_sorted = moderna_before.sort_values(by = ["Week of Allocations"], ascending = True)
moderna_sorted["Cumulative Allocations"] = moderna_sorted.groupby(["Jurisdiction"])["1st Dose Allocations"].apply(lambda x: x.cumsum())
moderna_data = moderna_sorted.merge(usmap, how = "left", on = "Jurisdiction")

pfizer_data["Week of Allocations"] = pfizer_data["Week of Allocations"].astype(str)
moderna_data["Week of Allocations"] = moderna_data["Week of Allocations"].astype(str)
