from django.shortcuts import render,get_object_or_404
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse,Http404


def corona_case_home_view(request):
	url = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true'
	data = requests.get(url)
	#print(data.status_code)  #Success
	corona_info = data.json()
	last_updated = corona_info['lastUpdatedAtApify'][:10]
	last_updated = last_updated.split("-")
	Year = last_updated[0]
	Month = last_updated[1]
	Date = last_updated[2]
	last_updated = Date +"-"+ Month +"-" + Year

	context = {
			"active_case": corona_info['activeCases'],
			"recovered": corona_info['recovered'],
			"death_case": corona_info['deaths'],
			"total_case": corona_info['totalCases'],
			"last_updated": last_updated,
			"region_data": corona_info['regionData'],
			"present_year": timezone.localtime().year
	}


	return render(request,'corona_info/corona_detail.html',context)
