#!/bin/python3

import requests
from datetime import datetime

from bs4 import BeautifulSoup

import pandas as pd

URL = "https://nl.wikipedia.org/wiki/Lijst_van_spoorwegstations_in_Nederland"

class StationScraper():
    def __init__(self):
        df_list = pd.read_html(URL, attrs = {'class': 'wikitable'},  flavor='bs4', thousands ='.')

        self.df = pd.concat(df_list, ignore_index=True, sort=False)

    def getNames(self):
        return list(self.df['Naam'])