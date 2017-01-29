import random
import requests

"""
TODO: we need to add a proxy url here....

"""
proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}
url = '' # Question URL


# Randomizing user agents
def LoadUserAgents():
    uas = []
    with open("./user_agents.txt", 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

while True:
    uas = LoadUserAgents()
    ua = random.choice(uas) 
    response = requests.get(url, proxies=proxy)
    print(response.text)
