n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
c=[]
for i in range(m):
	k=0
	d=b[i]-a[0]
	for j in range(n):
		if abs(b[i]-a[j])<d:
			k=j
			d=abs(b[i]-a[j])
	c.append(k)
for i in range(m):
	print(c[i],end=' ')
