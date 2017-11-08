#!/usr/bin/env python

#Import your CSV files into a single pandas.DataFrame() and plot the Republican
#vote share in Accomack County, Albermarle County, Alexandria City, and
#Alleghany County as a fraction of Total Votes Cast. Save your work as e3.py and
#commit your plots as: accomack_county.pdf, albemarle_county.pdf,
#alexandria_city.pdf, and alleghany_county.pdf.

#Imports

import requests
from bs4 import BeautifulSoup as bs
import argparse
import sys
import json
import pandas as pd
import glob
import matplotlib.pyplot as pls


#Accessing all election data files and initializing storage variables for loop.

allFiles= glob.glob("*.csv")
frame = pd.DataFrame()
datalist=[]

#Iterating through each election .csv, specifying 2nd row as header (has dem/rep
#info), dropping empty columns, creating column w/election year, and
#keeping only columns of interest to us.
#Putting all of this into one dataframe.

for f in allFiles:
    header = pd.read_csv(f, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(f, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = f[-8:-4:1]
    df2=df[0:5]
    mask=['Democratic', 'Republican', 'Total Votes Cast', 'Year']
    df3=df2[mask]
    datalist.append(df3)
frame=pd.concat(datalist)

#Dividing the # of republican votes by the total votes cast to get the proportion
#of votes per county that were republican.

frame['Republican Share'] = frame['Republican']/frame['Total Votes Cast']

#Length of frame is 120.
print(len(frame))

#Accomack county is at index 0 and reappears every 5 counties. So on and so forth
#for the others, always appearing in the same order.
Acc=frame[0:120:5]
Alb=frame[1:120:5]
Ale=frame[2:120:5]
All=frame[3:120:5]
Ame=frame[4:120:5]


#Getting figures and Saving

AccPlot=Acc.plot(x='Year', y='Republican Share', kind='bar', title= r'Proportion of Republican Votes in US Presidential Elections' + "\n" + 'Accomack County, 1924-2016')
AccPlot.set_xlabel("Year")
AccPlot.set_ylabel("% of Total Votes that were Republican")
AccPlot.get_figure().savefig('accomack_county.pdf', format='pdf')

AlbPlot=Alb.plot(x='Year', y='Republican Share', kind='bar', title= r'Proportion of Republican Votes in US Presidential Elections' + "\n" + 'Albemarle County, 1924-2016')
AlbPlot.get_figure().savefig('albemarle_county.pdf', format='pdf')
AlbPlot.set_xlabel("Year")
AlbPlot.set_ylabel("% of Total Votes that were Republican")

AlePlot=Ale.plot(x='Year', y='Republican Share', kind='bar', title= r'Proportion of Republican Votes in US Presidential Elections' + "\n" + 'Alexandria City, 1924-2016')
AlePlot.get_figure().savefig('alexandria_city.pdf', format='pdf')
AlePlot.set_xlabel("Year")
AlePlot.set_ylabel("% of Total Votes that were Republican")

AllPlot=All.plot(x='Year', y='Republican Share', kind='bar', title= r'Proportion of Republican Votes in US Presidential Elections' + "\n" + 'Alleghany County, 1924-2016')
AllPlot.get_figure().savefig('alleghany_county.pdf', format='pdf')
AllPlot.set_xlabel("Year")
AllPlot.set_ylabel("% of Total Votes that were Republican")

AmePlot=Ame.plot(x='Year', y='Republican Share', kind='bar', title= r'Proportion of Republican Votes in US Presidential Elections' + "\n" + 'Amelia County, 1924-2016')
AmePlot.get_figure().savefig('amelia_county.pdf', format='pdf')
AmePlot.set_xlabel("Year")
AmePlot.set_ylabel("% of Total Votes that were Republican")
