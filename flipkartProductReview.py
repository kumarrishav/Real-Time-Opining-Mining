#review on flipkart

import requests
import time
from bs4 import BeautifulSoup
 

for page in range(0,2000):
	url_raw = 'http://www.flipkart.com/lenovo-vibe-p1/product-reviews/ITMECHK5WMGKXKYQ?pid=MOBEB3VWYDTEM5QW&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=' 
	#'http://www.flipkart.com/apple-iphone-6s/product-reviews/ITMEBYSGQQARANAS?pid=MOBEBY3VG2Z2HVGJ&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_recent&start='
	url = url_raw + str(page * 10)

	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)

	review = soup.find_all("div", class_="fclear fk-review fk-position-relative line ")


	if not review:
		break

	print "#############################PAGE-" + str(page) + "#####################################"

	for row in review:
		star = row.find("div", class_="fk-stars")
		author = row.find("span", class_="fk-color-title fk-font-11 review-username")
		
		if not author:
			author = row.find('a', class_="load-user-widget fk-underline")

		date = row.find("div", class_="date line fk-font-small")
		title = row.find("div", class_="line fk-font-normal bmargin5 dark-gray")
		reviewer_review = row.find("span", class_="review-text")

		print star['title']
		print author.text.encode('utf-8')
		print date.text.encode('utf-8')
		print title.text.encode('utf-8')
		print reviewer_review.text.encode('utf-8')
		print '\n'

	print '\n'
	time.sleep(2)