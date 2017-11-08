#!/usr/bin/env python

#Using BeautifulSoup (docs), print, then save as ELECTION_ID, a list containing
#the years and election IDs in exactly this format.


#Imports
import requests
from bs4 import BeautifulSoup as bs
import argparse
import sys
import json
import pandas as pd


#Setting up variables to call in order to access the data.
url = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(url)
html = resp.content
soup = bs(html, "html.parser")


#Locating all the instances of "tr" AND class type "election_item" in the html code.
#Combo of "tr" and "election_type" uniquely identifies the rows of data we want (election IDs).
tags = soup.find_all('tr','election_item')

years = []
years_id = []
ELECTION_ID=[]


#Storing all of the year/id pairs in a list called "ELECTION_ID"
for t in tags:
    year = int(t.td.text)
    years.append(year)
    year_id = int(t['id'][-5:])
    years_id.append(year_id)
elections = [years, years_id]


#Creating a dataframe for the election years and ids
ELECTION_ID= pd.DataFrame({"years":years, "years_id":years_id})


#Saving the election data to a .txt file. Saved pandas dataframe.
ELECTION_ID.to_csv('ELECTION_ID.txt', sep='\t', index=False, header=False)

#Alternative, saved nested list:
#with open('ELECTION_ID_list.txt', 'w') as f:
    #f.writelines("%s\n" % line for line in elections)


#Printing the election date and ID data (ELECTION_ID.txt).
f = open('ELECTION_ID.txt','r')
electionIDlist = f.read()
print(electionIDlist)
f.close()


#This prints the dates and election ids, but doesn't store them all in the
#same list.
#for t in tags:
    #year = int(t.td.text)
    #year_id = int(t['id'][-5:])
    #ELECTION_ID = [year, year_id]
    #print(ELECTION_ID)
