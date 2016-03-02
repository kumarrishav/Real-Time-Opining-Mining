#review on amazon

import requests
from bs4 import BeautifulSoup

product_no = 'B016QBTFZC' # moto_turbo 'B019BH7V0O' iphone 'B016QBTFZC' 

#possible option for scarping : 
#&showViewpoints=1&filterByStar=all_stars&pageNumber=1&sortBy=recent
#&sortBy=recent&reviewerType=avp_only_reviews
#&sortBy=helpful&reviewerType=all_reviews
#&filterByStar=four_star&pageNumber=1
#&filterByStar=positive
#&filterByStar=critical


for page in range(1,100):
	url = 'http://www.amazon.in/product-reviews/'+ product_no +'/?ie=UTF8&showViewpoints=1&sortBy=recent&pageNumber=' + str(page)
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	review = soup.find_all("div", class_="a-section review")

	if not review:
		break

	print "#############################PAGE-" + str(page) + "#####################################"

	for row in review:
		star = row.find("span", class_="a-icon-alt")
		title = row.find("a", class_="a-size-base a-link-normal review-title a-color-base a-text-bold")
		author = row.find("a", class_="a-size-base a-link-normal author")
		date = row.find("span", class_="a-size-base a-color-secondary review-date")
		reviewer_review = row.find("span", class_="a-size-base review-text")

		print star.text.encode('utf-8')
		print title.text.encode('utf-8')
		print author.text.encode('utf-8')
		print date.text.encode('utf-8')
		print reviewer_review.text.encode('utf-8')
		print '\n'

	print '\n'
