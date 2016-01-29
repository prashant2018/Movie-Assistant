import requests,json
movie = input("Enter Movie Name : ")
url = "http://www.omdbapi.com/?"

r = requests.post(url,params={"tomatoes":"true","t":movie})
#r = requests.get(url+"t="+movie)
jformat =json.loads(r.text)

data = {

"Title":jformat["Title"],
"Plot":jformat["Plot"],
"Year":jformat["Year"],
"imdbRating":jformat["imdbRating"],
"imdbVotes":jformat["imdbVotes"],
"review":jformat["tomatoConsensus"],
"tomatoMeter":jformat["tomatoMeter"],
"tomatoRating":jformat["tomatoRating"],
"tomatoUserRating":jformat["tomatoUserRating"],
"tomatoUserMeter":jformat["tomatoUserMeter"],
}

#def analyze(data):
	
		
	
	
for item in data.values(): 
	print(item)



