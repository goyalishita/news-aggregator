import requests
from bs4 import BeautifulSoup as BSoup

session = requests.Session()
session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
url = "https://www.theonion.com/"
content = session.get(url,verify=False).content
soup = BSoup(content,"html.parser")
print("starting")
#News = soup.find_all('article', {"class":"sc-1pw4fyi-7 bsQJmS js_post_item"})
N = soup.find_all('section', {"class": "sc-1whp23a-2 exAeEH"})
N=N[1:]
for sections in N:
    #print(sections.prettify)
    News=sections.find_all('article')
    for article in News:
        print(article)
        a = article.div.a.div
        if a is not None:
            aa=a.div.div
            print(aa)
            imgg=str(aa.find('img')['srcset']).split(" ")[-4]
        else:
            continue
        # print(article.prettify)
        # for_img=article.find('div', {"class":"sc-1dm5z0l-0 chitzQ"})
        # img=""
        # if for_img is not None:
        #     img = str(for_img.find('img')['srcset']).split(" ")[-4]
        # else:
        #     img=None
        title=article.find('h4', {"class":"sc-1qoge05-0 gtIwiT"}).text
        print(title)
        for_link=article.find('div',{"class":"sc-1pw4fyi-3 ziaet"})
        link=""
        if for_link is not None:
            link = str(for_link.find('a')['href'])
        else:
            link=str(article.find('a')['href'])

        print(link)
        print(title)
        print(img)
        print('-------------------------------------------------------------------------------------')