from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup as BSoup
from .models import *

def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content = session.get(url,verify=False).content
    soup = BSoup(content,"html.parser")

    #News = soup.find_all('article', {"class":"sc-1pw4fyi-7 bsQJmS js_post_item"})
    N = soup.find_all('section', {"class": "sc-1whp23a-2 exAeEH"})
    N=N[1:]
    for sections in N:
        News=soup.find_all('article', {"class":"sc-1pw4fyi-7 bsQJmS js_post_item"})
        for article in News:
            for_img=article.find('div', {"class":"sc-1dm5z0l-0 chitzQ"})
            img=""
            if for_img is not None:
                img = str(for_img.find('img')['srcset']).split(" ")[-4]
            else:
                continue
            title=article.find('h4', {"class":"sc-1qoge05-0 gtIwiT"}).text
            for_link=article.find('div',{"class":"sc-1pw4fyi-3 ziaet"})
            link=""
            if for_link is not None:
                link = str(for_link.find('a')['href'])
            else:
                link=str(article.find('a')['href'])
            headlines = Headline.objects.all()
            l=[]
            for h in headlines:
                l.append(h.title)
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = img
            if title not in l:
                new_headline.save()
        return redirect("/")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/home.html", context)

