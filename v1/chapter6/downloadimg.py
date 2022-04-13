from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com')

# html.parser doesn't work
#bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html)

# imageLocation : 
# >>> bs.find('img')['src']
# 'https://pythonscraping.com/wp-content/uploads/2021/08/home1.jpg'
imageLocation = bs.find('img')['src']

#This downloads the logo from http://pythonscraping.com and stores it as logo.jpg in
#the same directory from which the script is running.
urlretrieve (imageLocation, 'logo.jpg')