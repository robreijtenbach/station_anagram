#!/bin/python3

from datetime import datetime
from bs4 import BeautifulSoup

import pandas as pd
import pickle
import os

URL = "https://nl.wikipedia.org/wiki/Lijst_van_spoorwegstations_in_Nederland"

class StationScraper():
    def __init__(self):
        datestring = f"{datetime.now():%Y-%m-%d}"
        
        renew = False

        pickles = [x for x in os.listdir() if ".pickle" in x]
        if len(pickles):
            pickles.sort(reverse=True)
            recent = pickles[0]
            
            if recent.split("-")[:2] != datestring.split("-")[:2]:
                renew = True
            else:
                with open(recent, 'rb') as f:
                    self.df = pickle.load(f)
        else:
            renew = True
        
                
        if renew:                
            try:
                df_list = pd.read_html(URL, attrs = {'class': 'wikitable'},  flavor='bs4', thousands ='.')
                self.df = pd.concat(df_list, ignore_index=True, sort=False)
                with open(f"stations_{datestring}.pickle", "wb") as f:
                    pickle.dump(self.df, f)
            except:
                pass

    def getNames(self):
        return list(self.df['Naam'])