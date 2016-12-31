import time
import random
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Firefox()

def login():
    browser.get('https://stackoverflow.com/users/login')
    email = browser.find_element_by_id("email")
    password = browser.find_element_by_id("password")
    email.send_keys("youremail")
    password.send_keys("yourpassword")
    browser.find_element_by_id("submit-button").click()
    time.sleep(2)

def upvoteqn(url):
    browser.get(url)
    browser.find_elements_by_class_name("vote-up-off")[0].click()


def select_page(a):   
    url="https://stackoverflow.com/questions?page="+str(a)+"&sort=votes"
    html = urlopen(url)
    bsObj = BeautifulSoup(html,"html5lib")
    que= bsObj.find_all("div", class_="question-summary")
    for div in que:
        link="https://stackoverflow.com"+div.a.get('href')
        result.append({'link': link})    

result = []
login()
s=random.randrange(1,100)
select_page(s)
for i in range(1,31):
    url=result[i]['link']
    print (url,s)
    upvoteqn(url)
