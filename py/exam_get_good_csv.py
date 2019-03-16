import os
import csv

goodfile = 0
#path = "/home/truename/python/sample/"#==43
path = "/home/truename/python/data/"
csvfiles = [os.path.join(root, name)
             for root, dirs, files in os.walk(path)
             for name in files
             if name.endswith((".csv"))]
for ff in csvfiles:
	with open(ff) as f:
		reader = csv.reader(f)
		r = next(reader)
		if "pet" in [x.lower() for x in r]:
			#print(ff)
			colmn=[x.lower() for x in r].index("pet")
			#print(r,colmn)
			dog=0
			cat=0
			for row in reader:
				if "dog" == row[colmn].lower():
					dog+=1
				if "cat" == row[colmn].lower():
					cat+=1
			if dog>cat:
				goodfile+=1
print(goodfile)
#dog>cat
