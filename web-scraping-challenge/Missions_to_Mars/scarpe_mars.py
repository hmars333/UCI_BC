#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from splinter import Browser
import time


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser= init_browser()

##NASA_NEWS##
url= 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)
time.sleep(1)

#connect to browser, create beautifulSoup object to parse through HTML
html = browser.html
soup = bs(html, 'html.parser')
type(soup)



##NEWS_TITLES##
news_title= soup.find('div', class_='content_title').get_text()
news_title



news_paragraph= soup.find('div',class_="article_teaser_body")
news_paragraph= news_paragraph.get_text()
browser.quit()
return news_title | news_paragraph


##JPL_IMAGE##
url2= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)


#connect to browser, create beautifulSoup object to parse through HTML
html = browser.html
soup2 = bs(html, 'html.parser')
type(soup2)



#clicks 'full size image' button
browser.click_link_by_id("full_image")
browser.url



#full image, source
image_source= browser.find_by_id("full_image")['data-link']
image_source
#full-size image url= base url + image source
featured_image_url= "'https://www.jpl.nasa.gov" + str(image_source)
featured_image_url



##MARS_WEATHER##
url3= 'https://twitter.com/marswxreport?lang=en'
browser.visit(url3)

html=browser.html
soup3= bs(html, 'html.parser')


#weather tweet
mars_weather= soup3.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_weather


##MARS_FACTS##
url4= 'https://space-facts.com/mars/'
browser.visit(url4)



html= browser.html
soup4=bs(html, 'html.parser')



#pandas reading html table, first table on page
mars_table= pd.read_html(url4)
mars_fact= mars_table[0]

mars_fact


#rename columns, reset index
mars_fact.columns= ['Description', 'Value']
mars_facts= mars_fact.set_index('Description', inplace= False)
mars_facts


##MARS_HEMISPHERES##
url5= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url5)

html= browser.html
soup5=bs(html, 'html.parser')


#find first hemsphere's title
hemi1= soup5.find('div', class_='description')
hemi1_title= hemi1.a.text
hemi1_title

#click on first hemiphere's link
browser.click_link_by_partial_text('Cerberus')

#check to see what page we are on
browser.url

#find first image url
h1_url= browser.find_link_by_partial_href('cerberus')['href']
h1_url

#find second hemsphere's title
hemi2= soup5.find_all('div', class_='description')[1]
hemi2_title= hemi2.a.text
hemi2_title

#click on second hemiphere's link
browser.click_link_by_partial_text('Schiaparelli')

#check page
browser.url

#find second image url
h2_url= browser.find_link_by_partial_href('schiaparelli')['href']
h2_url


#find third hemisphere's title
hemi3= soup5.find_all('div', class_='description')[2]
hemi3_title= hemi3.a.text
hemi3_title

#find third image url
h3_url= browser.find_link_by_partial_href('syrtis')['href']
h3_url

#find fourth hemisphere's title
hemi4= soup5.find_all('div', class_='description')[3]
hemi4_title= hemi4.a.text
hemi4_title

#find third image url
h4_url= browser.find_link_by_partial_href('valles')['href']
h4_url

##SAVE TO DICTIONARY##
hemisphere_image_urls= [{"Title": hemi1_title, "Image URL": h1_url},
                       {"Title": hemi2_title, "Image URL": h2_url},
                       {"Title": hemi3_title, "Image URL": h3_url},
                       {"Title": hemi4_title, "Image URL": h4_url}]

hemisphere_image_urls






browser.quit()
return news_title, news_paragraph | featured_image_url | hemisphere_image_urls




