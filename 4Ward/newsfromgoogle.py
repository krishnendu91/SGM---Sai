#!/usr/bin/python3

import pymysql
from pymysql import Error
from GoogleNews import GoogleNews

# Function to fetch news articles and store in MySQL table
def fetch_and_store_news():
    # Establish a connection to the MySQL database
    connection = pymysql.connect(host='localhost',database='4ward',user='admin',password='admin')
    # Create a cursor
    cursor = connection.cursor()
   # Initialize GoogleNews instance
    gn = GoogleNews(lang='en')
    # Search for news articles related to water quality
    gn.search('water quality in India')
    # Get search results
    search_results = gn.results()
    print(search_results)
    for result in search_results:
        date = result['date']
        source = result['media']
        title = result['title']
        url = result['link']
        
        insert_query = "INSERT INTO newsfromgoogle (date, source, title, url) VALUES (%s, %s, %s, %s)"
        data = (date, source, title, url)
        cursor.execute(insert_query, data)
        connection.commit()
        print("News articles fetched and stored successfully")
        connection.close()
        print("MySQL connection closed")

# Call the function to fetch and store news articles
fetch_and_store_news()
