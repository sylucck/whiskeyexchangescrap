from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models
from django.core.paginator import Paginator

# Create your views here.
baseurl = "https://www.thewhiskyexchange.com"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
base_url = "https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={}&psize=24&sort=pas"


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    #models.Search.objects.create(search=search)
    #print(quote_plus(search))
    for x in range(1,6):
        #final_url = base_url.format(quote_plus(search))
        result = requests.get(base_url.format(x))
        data = result.text
        soup = BeautifulSoup(data, features='html.parser')
        productlist = soup.find_all("li",{"class":"product-grid__item"})


        for product in productlist:
            link = product.find("a", {"class":"product-card"}).get('href')
            productlinks.append(baseurl + link)

    
    final_postings = []



    for link in productlinks:
        new_data = requests.get(link,headers=headers).text
        new_soup = BeautifulSoup(new_data,'html.parser')

        

        try:
            price= new_soup.find("p",{"class":"product-action__price"}).text.replace('\n',"")
        except:
            price = None

        try:
            about = new_soup.find("div",{"class":"product-main__description"}).text.replace('\n',"")
        except:
            about=None

        try:
            rating = new_soup.find("div",{"class":"review-overview"}).text.replace('\n',"")
        except:
            rating = None

        try:
            link = new_soup.find("a", {"class":"product-card"}).get('href')
            url_real = baseurl + link
        
        except:
            url_real = None

        try:
            name = new_soup.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
        except:
            name=None

        final_postings.append((name,url_real, price, about, rating))


    
    front_end = { 
        'search': search,
        'final_postings': final_postings,
    }
    return render(request,'myapp/new_search.html', front_end)