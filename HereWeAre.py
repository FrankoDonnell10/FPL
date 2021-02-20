#Using other .py file that works to try get h2h league data
#API Url returns correct values but only for row 6?
#Trying to return the 4 selected headers correctly before adjusting to what i actually need

#Import Libraries
import requests
import pandas as pd
import openpyxl

#Create Excel Worksheet
global g_w
wb = openpyxl.Workbook()
sheet0 = wb.create_sheet(index=0, title='Read_Me')
sheet1 = wb.create_sheet(index=1, title='2019_2020')

#Create Read me sheet
sheet0['B2'].value = 'Welcome to FPL data'

#Import API data and retrieve team name
url = "https://fantasy.premierleague.com/api/leagues-h2h-matches/league/585139/?event=1"
json_history = requests.get(url).json()

# Import gameweek history and insert data in sheet
header1 = ['GW', 'HName', 'AName', 'Htotal', 'Atotal']
headerrow = 1
for key in range(5):
    sheet1.cell(row=headerrow, column=key + 3).value = str(header1[key])

# To make a list of overall rank for inserting change in rank symbols
for each in json_history["results"]:
    g_w = each['event']
    Home = each['entry_1_name']
    Away = each['entry_2_name']
    Result1 = each['entry_1_total']
    Result2 = each['entry_2_total']

history_list = [g_w, Home, Away, Result1, Result2]
for rownum in range(g_w + 1, g_w + 2):
    sheet1.cell(row=rownum, column=3).value = g_w
for rownum in range(g_w + 1, g_w + 2):
    sheet1.cell(row=rownum, column=4).value = Home
for rownum in range(g_w + 1, g_w + 2):
    for key in range(2, 5):
        sheet1.cell(row=rownum, column=key + 3).value = history_list[key]

#Save Workbook
wb.save("Hereweare.xlsx")

