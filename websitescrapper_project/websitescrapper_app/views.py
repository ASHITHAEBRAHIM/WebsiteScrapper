import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import Links
# Create your views here.
def home(request):
    if request.method == "POST":
        link_new = request.POST.get('page','')
        urls = requests.get(link_new)
        beauty_soup = BeautifulSoup(urls.text,"html.parser")
        for link in beauty_soup.findAll('a'):
            li_address = link.get('href')
            link_name = link.string
            Links.objects.create(address=li_address,stringname=link_name)
        return HttpResponseRedirect('/')
    data_values = Links.objects.all()
    return render(request,"home.html",{"data_values":data_values})