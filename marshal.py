import json
import re
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
result = []
def find_bad_qn(a):
	url="https://stackoverflow.com/questions?page="+str(a)+"&sort=newest"
	html = urlopen(url)
	bsObj = BeautifulSoup(html,"html5lib")
	que= bsObj.find_all("div", class_="question-summary")
	for div in que:
		vote=int(div.find('span').text.split(' ')[0])
		link=div.a.get('href')
		name=div.a.text
		if(vote<-2 and not bool(re.search('(\[on hold\]|\[duplicate\]|\[closed\])$', name))):
		    result.append({'link': link, 'vote': vote,'name':name})

for i in range(50,70):
	find_bad_qn(i)

for qn in result:
	qn['link']="https://stackoverflow.com"+qn['link']	

result = json.dumps({'result': sorted(result, key=lambda x: x['vote'], reverse=False)})	
result=json.loads(result)
print("Please Wait.. it will take some time")
for qn in result['result']:
	print(qn['link']," Votes :", qn['vote'])
	url=qn['link']
	webbrowser.open(url, new=0, autoraise=True)

