from bs4 import BeautifulSoup

from urllib.request import urlopen
textPage = urlopen(
             'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(textPage.read())

#decode with 'utf-8'
textPage = urlopen(
             'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(str(textPage.read(), 'utf-8'))

'''
in the case of HTML pages, the encoding is usually contained in a tag
found in the <head> section of the site. Most sites, 
particularly English-language sites, have this tag:
	<meta charset="utf-8" />
Whereas the ECMA International’s website has this tag: 3
	<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=iso-8859-1">
If you plan on doing a lot of web scraping, particularly of international sites, 
it might be wise to look for this meta tag and use the encoding it recommends 
when reading the contents of the page.
'''

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bs = BeautifulSoup(html, "html.parser")
content = bs.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)