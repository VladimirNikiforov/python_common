n=int(input())
k1a = [i for i in input().split()]
k1 = k1a[0]
k1a.pop(0)
k2a = [i for i in input().split()] #map(int, input().split())
k2 = k2a[0]
k2a.pop(0)
x=0
while k1a and k2a:
	x += 1
	a, b = k1a.pop(0), k2a.pop(0)
	#print(x,a,b,k1a,k2a)
	if a > b:
		#print('a>b')
		k1a += [b, a]
	else:
		k2a += [a, b]
	if x == 1000000:
		print(-1)
		break
if x != 1000000:
	print(x,1 if k1a else 2)
