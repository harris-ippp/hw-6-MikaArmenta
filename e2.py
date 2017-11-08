#!/usr/bin/env python

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

#Storing all of the election years and  ids in lists called 'years' and 'years_id'
# to feed into 'base' url.

tags = soup.find_all('tr','election_item')
years = []
years_id = []
base= 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'

for t in tags:
    year = int(t.td.text)
    years.append(year)
    year_id = int(t['id'][-5:])
    years_id.append(year_id)


#Looping through years and years_id to retrieve data from other election years'
for line, name in zip(years_id, years):
    yearURL= base.format(line)
    yearText=requests.get(yearURL).text
    filename= "president_general_"+ str(name) + ".csv"
    with open(filename, "w") as out:
        out.write(yearText)


#The 2016 data that is required for this homework is saved under "president_general_2016.csv"
