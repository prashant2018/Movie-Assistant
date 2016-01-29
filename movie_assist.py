import sys,requests,json
movie = input("Enter Movie Name : ")
url = "http://www.omdbapi.com/?"
#http://www.omdbapi.com/?t=the martian&tomatoes=true
r = requests.post(url,params={"tomatoes":"true","t":movie})
#r = requests.get(url+"t="+movie)
jformat =json.loads(r.text)
li=["Title","Plot","Year","imdbRating","imdbVotes","tomatoConsensus","tomatoMeter","tomatoRating","tomatoUserRating","tomatoUserMeter"]
class MovieData(object):		
	
	def __init__(self,jformat,li):
		
		self.jformat=jformat	
		self.data={}	
		self.li=li
		for i in self.li:
			self.data.setdefault(i,"N/A")
		try:				
			self.data = {
			"Title":self.jformat["Title"],
			"Plot":self.jformat["Plot"],
			"Year":self.jformat["Year"],
			"imdbRating":self.jformat["imdbRating"],
			"imdbVotes":self.jformat["imdbVotes"],
			"tomatoConsensus":self.jformat["tomatoConsensus"],
			"tomatoMeter":self.jformat["tomatoMeter"],
			"tomatoRating":self.jformat["tomatoRating"],
			"tomatoUserRating":self.jformat["tomatoUserRating"],
			"tomatoUserMeter":self.jformat["tomatoUserMeter"],
			}
			
		except:	
			print("No Movie Found")
			k = 1
	
		for i in self.li:
			if self.data[i] == "N/A":
				self.data[i] = 0
	
		
		
	def show(self):
		for k,v in self.data.items():
			if v != 0:
				print(k+" : "+v)
	
mv = MovieData(jformat,li)
mv.show()		
	
	
#for item in data.values(): 
#	print(item)



