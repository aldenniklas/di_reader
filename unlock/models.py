from __future__ import unicode_literals
from django.db import models
import requests
from bs4 import BeautifulSoup

# Function for printing articles    
    
def print_article(site_url):
    output_format = 2
    
    raw_html = requests.get(site_url).content
    soup = BeautifulSoup(raw_html, "html.parser")
    
    article_content = {
        "title": soup.find('h1', class_='di_article-top__heading').prettify(),
        #"img": soup.picture.get('srcset'),
        "txt": soup.find('div', class_='di_article-content').prettify()
    }
    
    return article_content