from django.http import HttpResponse
from django.shortcuts import render
import requests, json


def index(request):
    content = requests.get('https://restcountries.eu/rest/v2/all')
    countryinfolist = content.json()

    country_list = []
    for country in countryinfolist:
        country_list.append(country)
    return render(request, 'index.html', {
        'countries': country_list
    })
        #           {
        # 'country': countryinfo['name'],
        # 'capital': countryinfo['capital'],
        # 'continent': countryinfo['region'],
        # 'currency': countryinfo['currencies'],
        # 'flag': countryinfo['flag']
        #
        # }
        #           )

def anthem(request):
    print('trutututu')
    # play anthem with javascript
    # return render(request, 'index.html')

