# https://ideone.com/KGYDob

import sys
prev = ''
avert = []
for line in sys.stdin:
	vert,dist,vs = line.split()
	if (vert != prev) and (prev != ''):
		print(prev+'\t'+"{:.3f}".format(0.02+0.9*avert[0])+'\t'+avert[1])
		if vs == '{}':
			avert = [float(dist),vs]
		else:
			avert = [0,vs]
		prev = vert
	else:
		prev = vert
		if len(avert) > 0:
			if vs == '{}':
				avert[0] += float(dist)
			else:
				avert = [avert[0],vs]
		else:
			if vs == '{}':
				avert = [float(dist),vs]
			else:
				avert = [0,vs]
print(prev+'\t'+"{:.3f}".format(0.02+0.9*avert[0])+'\t'+avert[1])

'''
1	0.067	{}
1	0.200	{2,4}
2	0.067	{}
2	0.100	{}
2	0.200	{3,5}
3	0.067	{}
3	0.100	{}
3	0.200	{4}
4	0.100	{}
4	0.200	{}
4	0.200	{5}
5	0.100	{}
5	0.200	{}
5	0.200	{1,2,3}
'''



v = int(input())
t = int(input())
if v >= 0:
	l = (v*t)%109
else:
	if t > 0:
		l = 109+((v*t)%(-109))
	else:
		l = 0
if l = 109:
	l = 0
print(str(l))


h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
c = (h2*3600 + m2*60 + s2)-(h1*3600 + m1*60 + s1)
print(str(c))

n = int(input())
h = (n//3600)%24
m = (n%3600)//60
s = (n%3600)%60
print(str(h)+':'+"{:02d}".format(m)+':'+"{:02d}".format(s))

a = int(input())
b = int(input())
n = int(input())
c = a*100 + b
na = (c*n)//100
nb = (c*n)%100
print(str(na)+' '+str(nb))