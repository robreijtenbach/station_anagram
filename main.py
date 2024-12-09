from anagram import Anagrams
from station_scraper import StationScraper

import random

s = StationScraper()

a = Anagrams(s.getNames())

print(a.getAnagram("Gillehom"))

ana = "".join(random.sample("krabbendijke", len("krabbendijke")))

print(ana)
print(a.getAnagram(ana))
