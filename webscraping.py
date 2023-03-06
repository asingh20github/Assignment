import pandas as pd
import numpy as np
import requests
from urllib.request import Request, urlopen
import ast
from bs4 import BeautifulSoup
from time import sleep
from random import randint

actor_name = []
movie_name = []
movie_list = []


#Function to iterate through different pages of the site
def checkpages():
    pages = np.arange(1,11,1)
    for page in pages:
        page = requests.get("https://www.imdb.com/list/ls058011111/?sort=list_order")
        soup = BeautifulSoup(page.text,'html.parser')
        actor_data = soup.findAll('div',attrs ={'class':'lister-item mode-detail'} )
        sleep(randint(2,8))
        page.close()
        for store in actor_data:
            name = store.h3.a.text
            name = name.rstrip("\n")
            actor_name.append(name)
            
        for store in actor_data:
            link_url = store.find_all("a")[1]["href"]
#     print(f"Apply here: {link_url}\n")
            a = str("https://www.imdb.com")+link_url+str("?ref_=nmls_kf")
            movie_name.append(a)
        # print(movie_name)
    
        data_combined = dict(zip(actor_name,movie_name))
        movie_data = str(data_combined)
        m_data = ast.literal_eval(movie_data)
    return m_data
#Function to iterate the keys of dictionary which gives the actor's page link as values and then use that link to find the movie names of that page.
def checkKey(dict, key):  
    # print(key)
    # print(dict)    
    if key in dict:
        movie_link = dict[key]
        n = str(movie_link)
        # print(n)
        #Using the link of actor's page to access the movie names and print 
        # movie_data_1 =requests.get(str(movie_link)) 
        # hdr = {'User-Agent': 'Mozilla/5.0'}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
# }headers={'content-type': 'application/json; charset=utf-8'},
        page = requests.get(n, headers=headers)
        # page = urlopen(req)
        soup1 = BeautifulSoup(page.text,"html.parser")
        
        # print(soup1)
        # movie_data_1 = soup1.findAll('div',attrs={'class':['filmo-row odd','filmo-row even']})
        movie_data_1 = soup1.findAll('li',attrs={'class':['ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click sc-139216f7-1 fFMbUG']})
        # print(movie_data_1)
        sleep(randint(2,8))
    
        for store_1 in movie_data_1:
            name_1 = store_1.find('a',attrs={'class':['ipc-metadata-list-summary-item__t']}).text
            # name_1 = name_1.rstrip("\n")
            movie_list.append(name_1)
        # 
        movie_list.sort(reverse=True)   
        print(movie_list)

    else:
        print("Actor not present in the list")
# print("Inside main")
act_name = input()

# page = urlopen("https://www.imdb.com/name/nm0000134/?ref_=nmls_kf")

# act_name print= "Robert De Niro"
# (act_name)
data_movies = checkpages()        
movie_list =[]
act_name1= " "+act_name
checkKey(data_movies,act_name1)
