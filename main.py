


import xml.etree.ElementTree as etree

#-------------------------load data sources
### craigslist by city/state
url_tree = etree.parse("urls.xml")
url_root = url_tree.getroot()

print("url_root: {0}".format(url_root))


###  autotrader
### truecar
### dealerships
### cars.com
### list of cars


#-------------------------scrape the web

