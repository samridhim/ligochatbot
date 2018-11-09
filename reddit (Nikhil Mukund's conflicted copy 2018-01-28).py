import requests 
import json
import pprint
conversation = []
f = open('data.txt','w')
f1 = open('replies.txt', 'w')
r = requests.get('https://www.reddit.com/r/IAmA/comments/45g8qu/we_are_the_ligo_scientific_collaboration_and_we/.json?t=all&limit=500', headers = {'User-agent': 'Chrome'})
theJSON = json.loads(r.text)[1]
data = (theJSON['data']['children'])
print len(data)
for d in data:
	comm = (d['data'])
	if(len(comm)==47):
		f.write("Question : " + comm['body'].encode('utf-8') + "\n\n")
		conversation.append(comm['body'])
		if(type(comm['replies'])==dict):
			rr = comm['replies']
			dd = rr['data']['children']
			for ddd in dd:
				count =0
				repl = ddd['data']
				if(len(repl)==47):
					f.write("Answer : "+ repl['body'].encode('utf-8') + "\n\n")
					conversation.append(repl['body'])
					break;
f.close()
