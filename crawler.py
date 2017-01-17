import bs4 as bs
import urllib.request

def search(searchee = '960m'):
    result = urllib.request.urlopen('http://www.ebay.co.uk/sch/PC-Laptops-Netbooks/177/i.html?_sop=15&_from=R40&_oac=1&_nkw={0}&_ipg=200&rt=nc'.format(searchee)).read()
    soup = bs.BeautifulSoup(result, 'lxml')
    input('press any key to finish')
    resultFile = open('search_result{0}.txt'.format(searchee), 'a')
    links = soup.find_all('h3', class_='lvtitle')
    for i in links:
        appendMe = "\n" + str(i)
        resultFile.write(appendMe)
    resultFile.write(str(links))
    resultFile.close()


search()
