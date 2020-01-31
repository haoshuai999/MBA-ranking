import lxml
import requests
import sys
import random
import pandas as pd
from lxml.html import fromstring

def scrape(url, rank_array, business_school_array, country_array):


	user_agent_list = [
		"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
		"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
		"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
		"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML, likeGecko)Chrome / 17.0.963.56Safari / 535.11",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)",
		"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"
	]


	headers = {
		'User-Agent': random.choice(user_agent_list)
	}

	print(url)

	page_html_text = requests.get(url, headers=headers).text
	page_html = fromstring(page_html_text)
	ranks = page_html.cssselect(".views-field-field-wmba-school-rank-overall-value")[1:]
	for i in range(len(ranks)):
		rank_text = ranks[i].text_content().strip()
		rank_array.append(rank_text)
	schools = page_html.cssselect(".views-field-field-wmba-school-name-alpha-value a")[1:]
	for j in range(len(schools)):
		school_text = schools[j].text_content().strip()
		business_school_array.append(school_text)
	countries = page_html.cssselect(".views-field-name")[1:]
	for k in range(len(countries)):
		country_text = countries[k].text_content().strip()
		country_array.append(country_text)

	return (rank_array, business_school_array, country_array)

def set_parameter(year, page = 6):
	rank_array = []
	business_school_array = []
	country_array = []
	for i in range(int(page)):
		url = "https://www.economist.com/whichmba/full-time-mba-ranking?page=" + str(i) + "&year=" + year + "&term_node_tid_depth=77631"
		#count = 0
		#for url in urls:
		#count += 1
		rank_array, business_school_array, country_array = scrape(url, rank_array, business_school_array, country_array)
		#if count % 10 == 0:
		print("output csv...")
		df = pd.DataFrame(list(zip(rank_array, business_school_array, country_array)), columns=['Rank', 'Business_school', 'Country'])
		df.to_csv("MBA_ranking_" + year +".csv", index=False, encoding='utf-8-sig')

if __name__ == '__main__':
	year = sys.argv[1].lower()
	page = sys.argv[2].lower()
	set_parameter(year, page)
