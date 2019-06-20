#Vocab Grabber
#Nolan Clement
#6/19/2019
import requests
import json
#Settings for the Oxford Dictionary API
#https://developer.oxforddictionaries.com/          
#app_id and app_key can be found under API CREDENTIALS
app_id = "045f090f"
app_key = "1d331bf21e5de06b4cb199ba9b6fb4c5"
language = "en-gb"
#Initialize list to store wordlist
words = []
#Format for infile is one vocab word per line
infile = open("infile.txt", "r")
wordList = infile.readlines()
#Fills words with each vocab word
for x in wordList:
	words.append(x)
#Initialize Outfile
outfile = open("outfile.txt", "w")
#Iterate over each word
for word in wordList:
	#Remove the trailing newline
	word = word.rstrip('\n')
	#Make request to API
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word.lower()
	r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
	try:
		#Access definition portion of json data by indexing through the dictionary
		#Removes the default [' and ']
		jsonData = r.json();
		definiton = str(jsonData['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']).replace('[', '').replace(']','').replace("'", '')
	except:
		#Default to this if json data does not contain 'definitons'
		definiton = "No definition available."
	#Format definition and write to outfile
	outfile.write(word + " - " + definiton + "\n")










 
