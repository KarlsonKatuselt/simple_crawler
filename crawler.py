import bs4 as bs
import urllib.request

def url(searchee = '960m'):
    result = urllib.request.urlopen('http://www.ebay.co.uk/sch/PC-Laptops-Netbooks/177/i.html?_sop=15&_from=R40&_oac=1&_nkw={0}&_ipg=200&rt=nc'.format(searchee)).read()
    resultFile = open('search_result_{0}.txt'.format(searchee), 'a')
    return result, resultFile

def crawl_for_urls():
    result, resultFile =  url()
    soup = bs.BeautifulSoup(result, 'lxml')
    laptops = soup.find_all('h3', class_ = 'lvtitle')
    links = []
    
    for i in laptops:
        links.append(i.a('href'))
        print(i.a('href'))
        type(i.a('href'))

    resultFile.close()
    print(str(links))


crawl_for_urls()
