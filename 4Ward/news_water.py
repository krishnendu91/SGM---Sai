#!/usr/bin/python3

#importing necessary libraries
import requests_html
import requests

#uncomment on first run only
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

from lxml import html
from lxml.html.soupparser import fromstring

from urllib.parse import urlparse, urljoin
import urllib.request
import urllib.robotparser
import pandas as pd
import pymysql
from bs4 import BeautifulSoup
from newspaper import Article
import string
from datetime import date
from htmldate import find_date

#declaring lists globally
gnews_links = []               #list of URLs from google news
gnews_permitted = []           #list of URLs from google news that permit crawling
download_link = []             #list of URLs from google news that proceeded to download after succeeding content analysis

conn = pymysql.connect(user="4ward",password="Amma@123",database="4ward") #setting connection to sql
cur = conn.cursor()

def get_article(download_link):  #function to download articles using newspaper API
    list_title = []          #list of titles
    list_content = []        #list of contents
    list_source = []         #list of source URLs
    list_date = []           #list of dates
    list_summary = []        #list of summary
    list_img = []            #list of image URLs
    list_location = []

    titles = []
    print(download_link)
    for url in download_link:
        try:
            article = Article(url)
            article.download()
            article.parse()
            title = article.title
            print("downloading content from URL: ", url)
            list_title.append(title)
            print("article title found")
            content = article.text #extract paragraph of article
            list_content.append(content)
            print("article content found")
            pub_date = find_date(url) #date of article
            list_date.append(pub_date)
            print("article date found")
            article.nlp()
            #locationId = article.locationId #summary of article
            #list_location.append(locationId)
           # print("article summary found")
            #img = article.top_image #top image of article
            #list_img.append(img)
            #source = url #source url of article
            #list_source.append(source)
           # print("article source found")
            newdata = {'News_title' : list_title[0], 'News_content' : list_content[0], 'Published_Date' : list_date[0]}
            print(newdata)
            cur.execute("INSERT INTO `news_data` (`Title`,`Content`,`PublishDate`) VALUES (%(News_title)s, %(News_content)s, %(Published_Date)s);",newdata)
            conn.commit()
        
        except:
            pass
      
def checkRobots(links_list): #checking scraping permission of each URL passed
    permitted_links = []     #list of scraping permitted links
    links_list = list(dict.fromkeys(links_list))
    for url in links_list:
        robot_parse = urllib.robotparser.RobotFileParser() #calling urllib's robotparser function
        robot_url = url + "/robots.txt" #appending robots.txt to the end of every URL
        #internal codes of robotparser
        robot_parse.set_url(robot_url)
        robot_parse.read()
        response = robot_parse.can_fetch("*", url)
        if response is True: #if the robotparser function returns true, it means the website gives permission to scrape data
            permitted_links.append(url)
    return permitted_links

def trendingSearch(): #prepares query for searching in google news
    url_water_india = "https://news.google.com/search?q=water%20quality%20news%20in%20india&hl=en-IN&hl=en-IN&gl=IN&gl=IN&ceid=IN%3Aen" #link of the query "landslide in India" with today's date
    googleNews_scrape(url_water_india)
    url_water_erkm = "https://news.google.com/search?q=water%20quality%20news%20%20in%20ernakulam&hl=en-IN&gl=IN&ceid=IN%3Aen" #link of the query "flood in India" with today's date
    googleNews_scrape(url_water_erkm)


def googleNews_scrape(url): #function extracts all article links in google news
    r1 = requests.get(url) #sends request to webpage to access
    page = r1.text #collects source code of web page
    soup1 = BeautifulSoup(page, "html.parser")
    for link in soup1.find_all("a", class_="VDXfz"): #beautifulsoup function collects all anchor tags under the given class
        relative_link = (link.get('href')) #collects all href links under the given class
        full_link = relative_link.replace(relative_link[:1], "https://news.google.com") #since google news returns a "." instead of the domain name, need to replace it
        gnews_links.append(full_link)
    
def crawler():
    trendingSearch() #function call for google news search
    gnews_permitted = checkRobots(gnews_links) #function call to check if a webpage permits scraping or not
    get_article(gnews_permitted) #function call to download news articles
    print("............crawling completed................")

crawler()
