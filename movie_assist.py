import sys,requests,json

li=["Title","Plot","Year","imdbRating","imdbVotes","tomatoConsensus","tomatoMeter","tomatoRating","tomatoUserRating","tomatoUserMeter"]
li_show=["Title","Plot","Year","imdbRating","tomatoMeter"]

def search():
	movie = input("Enter Movie Name : ")
	url = "http://www.omdbapi.com/?"
	print()
	#http://www.omdbapi.com/?t=the martian&tomatoes=true

	try:
		r = requests.post(url,params={"tomatoes":"true","t":movie})
	except:
		print("Network Error !")
		search()
		return 0

	jformat =json.loads(r.text)
	
	return jformat
	
	
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
	
		
		
	#def show(self):
	#	for k,v in self.data.items():
	#		if v != 0:
	#			print(k+" : "+v)
	
	def show(self):
		self.li_show=li_show
		for k in self.li_show:
			if self.data[k] != 0:
				print(k+" : "+self.data[k]+'\n')
		print()
	
	def analyze(self):
		self.total=0
		self.temp=["imdbRating",'tomatoMeter','tomatoRating','tomatoUserRating']
		for i in self.temp:
			if self.data[i]==0:
				self.total = self.total + 0
			else:
				self.total=self.total+10
				self.data[i] = float(self.data[i])
		if self.total == 0:
			self.assist=-1
		else:
			self.assist = ((self.data['imdbRating']+(self.data['tomatoMeter']/10)+self.data['tomatoRating']+self.data['tomatoUserRating']*2 )/self.total)*10
		
		return self.assist
		
	
			
		
jformat = search()
if jformat == 0:
	jformat = search()
mv = MovieData(jformat,li)
mv.show()		

def verdict():
	assist = mv.analyze()
	if assist == -1:
		print("Ratings Not Available")
	elif assist >= 0 and assist <=2 :
		print("Never Watch it ! Just delete the Movie")	
	elif assist > 2 and assist <=3 :
		print("Simple Advise. Dont watch ")
	elif assist > 3 and assist <=4 :
		print("Waste your Time If you have it in plenty. ")		
	elif assist > 4 and assist <=5 :
		print("Watch at your own risk")
	elif assist > 5 and assist <=6 :
		print("Can watch but not recommended")
	elif assist > 6 and assist <=7 :
		print("OK OK")
	elif assist > 7 and assist <=8 :
		print("It's Good")
	elif assist > 8 and assist <=8.5 :
		print("Nice one. You should definetly watch it !")
	elif assist > 8.5 and assist <=9 :
		print("Very Good. Must Watch! Highly Recommended!")
	elif assist > 9 and assist <=10 :
		print("Awesome!.If you didn't watched this, you watched nothing. Best of all.")

print("-----------------------------------------------------------------------------------------------------------------------------","\n")
print("---------------------------------------------------------The Final Verdict------------------------------------------------")				
verdict()
print("-----------------------------------------------------------------------------------------------------------------------------","\n")	

