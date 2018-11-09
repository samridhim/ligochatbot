import requests 
import json
import pprint
conversation = []
f = open('data.txt','w')
f1 = open('replies.txt', 'w')
r = requests.get('https://www.reddit.com/r/IAmA/comments/45g8qu/we_are_the_ligo_scientific_collaboration_and_we/.json?t=all&limit=1000', headers = {'User-agent': 'Chrome'})
theJSON = json.loads(r.text)[1]
print theJSON.keys()
print theJSON['kind']
print theJSON['data'].keys()
data = (theJSON['data']['children'])
question =0
for d in data:
	comm = (d['data'])
	if(len(comm)==47):
		f.write("Question : " + comm['body'].encode('utf-8') + "\n\n")
		conversation.append(comm['body'])
		question = question+1
		if(type(comm['replies'])==dict):
			rr = comm['replies']
			dd = rr['data']['children']
			for ddd in dd:
				repl = ddd['data']
				if(len(repl)==47):
					f.write("Answer : "+ repl['body'].encode('utf-8') + "\n\n")
					conversation.append(repl['body'])
					break;
f.close()
