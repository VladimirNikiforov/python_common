"""
2.2 Числа Фибоначчи
Задача на программирование: небольшое число Фибоначчи
Дано целое число 1≤n≤401≤n≤40, необходимо вычислить nn-е число Фибоначчи (напомним, что F0=0F0=0, F1=1F1=1 и Fn=Fn−1+Fn−2Fn=Fn−1+Fn−2 при n≥2n≥2).
Sample Input:
3
Sample Output:
2

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    x=[]
    x.append(0)
    x.append(1)
    for i in range(2,n+1):
       x.append(x[i-1]+x[i-2])
    return x[n]

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()

------------ alternate
def fib(n):
	a,b=0,1
	yield a
	yield b
	for i in range(n-1):
		a,b=b,a+b
		yield b

print(list(fib(int(input())))[-1])


-------- alternate
def fib(num):

    prev, cur = 0, 1

    for i in range(1, num):
        prev, cur = cur, prev + cur

    return cur


def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()

"""
"""
Задача на программирование: последняя цифра большого числа Фибоначчи



Дано число 1≤n≤1071≤n≤107, необходимо найти последнюю цифру nn-го числа Фибоначчи.

Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением. 
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи: 
если 0≤a,b≤9 — последние цифры чисел Fi и Fi+1 соответственно, 
то (a+b)mod10 — последняя цифра числа Fi+2.

Sample Input:
132941
Sample Output:
1

def fib_digit(n):
    if n==0:
        return 0
    if n==1:
        return 1
    x=[]
    x.append(0)
    x.append(1)
    for i in range(2,n+1):
       x.append((x[i-1]%10+x[i-2]%10)%10)
    return x[n]

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

--------- alternate!
def fibd(n):
	a,b=0,1
	for i in range(n-1):
		a,b=b%10,(a+b)%10
	return b
		
print(fibd(int(input())))	


----------- alternate
def fib_digit(n):
    d = [0,1]
    [d.append((d.pop(0) + d[-1])%10) for i in range(2,n+1)]
    return d[-1]


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()

	
	
	
------- java alternate
import java.util.Scanner;
class Main {
  public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      int i = Integer.parseInt(sc.nextLine()) + 1;
      int[] f = new int[i];
      f[0] = 0;
      f[1] = 1;
      for(int j = 2; j < f.length; j++)
      {
          f[j] = (f[j-1] + f[j-2]) %10;
      }
      System.out.print(f[i-1]);
  }
}
"""

"""
Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа 1≤n≤10181≤n≤1018 и 2≤m≤1052≤m≤105, необходимо найти остаток от деления nn-го числа Фибоначчи на mm.

Sample Input:
10 2
Sample Output:
1

def fib_mod(n, m):
    x=[]
    x.append(0)
    x.append(1)
    for i in range(2,m*6):
	    x.append((x[i-1]+x[i-2])%m)
	    if (x[i]==1) & (x[i-1]==0): #this is a period!
	        break
    return x[(n%(len(x)-2))]

def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()

------------- alternate
n,m=map(int,input().split())
o,i=[0,1],2
while not (o[i-2]==0 and o[i-1]==1) or i<=2:
	o.append((o[i-2]+o[i-1])%m)
	i+=1
print(o[n%(i-2)])

-------------- alternate
n, MOD = map(int, input().split())

def mul(A,B):
    return [ [ sum(A[r][i]*B[i][c] for i in range(2))%MOD for c in range(2) ] for r in range(2) ]

def exp(A,n):
    if n==0: return [ [1,0], [0,1] ]
    C = exp(A,n//2)
    C = mul(C,C)
    return mul(A,C) if n%2 else C

print( exp( [ [0,1], [1,1] ], n )[0][1] ) 
http://codeforces.com/blog/entry/14516?locale=ru	
	
"""



"""
Задача на программирование: наибольший общий делитель
По данным двум числам 1≤a,b≤2⋅1091≤a,b≤2⋅109 найдите их наибольший общий делитель.
Sample Input 1:
18 35
Sample Output 1:
1
Sample Input 2:
14159572 63967072
Sample Output 2:
4

def gcd(a, b):
	if a==0:
		return b
	if b==0:
		return a
	if a>b:
		return gcd(a%b,b)
	else:
		return gcd(a,b%a)
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))
if __name__ == "__main__":
    main()
---------- alternate
x, y = sorted(map(int, input().split()))
while x:    
    y,  x = x, y % x
print(y)
------------ alternate
def gcd(a, b):
    while a:
        a, b = b % a, a
    return b
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))
if __name__ == "__main__":
    main()
----------- alternate
def gcd(a, b):
    return gcd(b, a % b) if b else a    
def main():
    a, b = map(int, input().split())
    print(gcd(a, b))
if __name__ == "__main__":
    main()
-------------- 
"""

"""
Задача на программирование: покрыть отрезки точками
По данным nn отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1≤n≤1001≤n≤100 отрезков. Каждая из последующих nn строк содержит по два числа 0≤l≤r≤1090≤l≤r≤109, задающих начало и конец отрезка. 
Выведите оптимальное число mm точек и сами mm точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3 
Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 


n = int(input())
x = [[int(x) for x in input().split()] for i in range(n)]
x.sort(key=lambda t: t[1])
m=[]
for i in x:
	f=0
	for k in m:
		if k >= i[0] and k <= i[1]:
			f=1
	if f==0:
		m.append(i[1])
print(len(m))
print(' '.join(str(k) for k in m))

----------------- alternate
segments = sorted([sorted(map(int,input().split())) for i in range(int(input()))], key=lambda x: x[1])
dots = [segments.pop(0)[1]]
for l, r in segments:
    if l > dots[-1]:
        dots.append(r)
print(str(len(dots)) + '\n' + ' '.join(map(str, dots)))

-------------- alternate
def greedy(lines):
    lines = sorted(lines, key = lambda x: x[1])
    l, r = lines.pop(0)
    dots = [r]
    for l, r in lines:
        if l <= dots[-1] <= r:
            continue
        else:
            dots.append(r)
    dots = list(map(str, dots))
    return str(len(dots)) + '\n' + ' '.join(dots)

def main():
    n = int(input())
    lines = []
    for i in range(n):
        line = list(map(int, input().split()))
        lines.append(line)
    print(greedy(lines))


if __name__ == "__main__":
    main()
-------------- alternate
from operator import itemgetter

segments = [tuple(map(int, input().split())) for _ in range(int(input()))]
segments.sort(key=itemgetter(1))

points = []
i = 0
while i < len(segments):
    cur = segments[i]
    points.append(cur[1])
    j = i + 1
    while j < len(segments) and cur[1] >= segments[j][0]:
        i = j
        j += 1
    i = j

print(len(points))
print(' '.join(map(str, points)))

"""

"""
Задача на программирование: непрерывный рюкзак



Первая строка содержит количество предметов 1≤n≤1031≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. 
Каждая из следующих nn строк задаёт стоимость 0≤ci≤2⋅1060≤ci≤2⋅106 и объём 0<wi≤2⋅1060<wi≤2⋅106 предмета (nn, WW, cici, wiwi — целые числа). 
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000

n,max = [int(x) for x in input().split()]
x = [[int(x) for x in input().split()] for i in range(n)]
x.sort(key=lambda t: t[0]/t[1], reverse=True)
s=0
while max and x:
	s+=x[0][0] if x[0][1]<=max else x[0][0]*max/x[0][1]
	if x[0][1]<max:
		max=max-x[0][1]
		x.pop(0)
	else:
		max=0
print(s)


------------- alternate
# put your python code here
n, W = map(int, input('').split())
l = sorted([tuple(map(int, input('').split())) for N in range(n)], key=lambda x: x[0]/x[1], reverse=True)
ans = 0.0
for i in l:
    if W == 0:
        break
    if i[1] <= W:
        ans += i[0]
        W -= i[1]
    else:
        ans += (i[0]/i[1]) * W
        W = 0
print('{0:.3f}'.format(ans))


----------------- alternate
n, W = map(int, input().split())
p = []
for i in range(n):
    c, w = map(int, input().split())
    if c * w > 0 : p.append([c ,w])
p.sort(key=lambda cw: cw[1]/cw[0] )
ans = []
weight_in_pack = 0
while weight_in_pack < W and len(p):
    i = p.pop(0)
    ans.append(i if i[1]<=(W - weight_in_pack) else [i[0]/i[1]*(W - weight_in_pack), (W - weight_in_pack)])
    weight_in_pack = sum([a[1] for a in ans])
print(sum([a[0] for a in ans]))
    
----------- alternate
def greedy(items, W):
    items = sorted(items, key = lambda x: x[0]/x[1], reverse = True)
    res = 0
    for c, w in items:
        if w <= W:
            res += c
            W -= w
        else:
            res += c * (W / w)
            break
    return '%.3f' %res

def main():
    n, W = list(map(int, input().split()))
    items = []
    for i in range(n):
        item = list(map(int, input().split()))
        items.append(item)
    print(greedy(items, W))


if __name__ == "__main__":
    main()

-------------------- alternate
N, space = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
items.sort(key=lambda x: x[0] / x[1], reverse=True)

total = 0
for item in items:
    if space >= item[1]:
        total += item[0]
        space -= item[1]
    else:
        total += space * (item[0] / item[1])
        break
        
print("{:.3f}".format(total))

"""

"""
Задача на программирование: различные слагаемые

По данному числу 1≤n≤1091≤n≤109 найдите максимальное число kk, для которого nn можно представить как сумму kk различных натуральных слагаемых. 
Выведите в первой строке число kk, во второй — kk слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3 
Sample Input 2:
6
Sample Output 2:
3
1 2 3 
----- time limit
n = int(input())
x = []
i = 1
while n:
	if ((not (i in x)) and (not ((n-i) in x))):
		x.append(i)
		n-=i
	i+=1
print(len(x))
print(' '.join(str(i) for i in x))
--- good

n = int(input())
x = []
i = 1
while n:
	if n>=i:
		x.append(i)
		n-=i
		i+=1
	else:
		x[-1]+=n
		break
print(len(x))
print(*x, sep=' ')

--- good
import math

n = int(input())
if n <= 2:
	print(1)
	print(n)
else:
	x = []
	k=math.trunc((-1+math.sqrt(1+8*n))/2)
	print(k)
	for i in range(1,k):
		x.append(i)
	x.append(n-math.trunc(k*(k-1)/2))
	print(' '.join(str(i) for i in x))

------------- alternate
n = int(input(''))
ans = [0]
i = 0
while n >= 0:
    i += 1
    if i >= (n -i):
        ans.append(n)
        ans[0] += 1
        break
    n -= i    
    ans.append(i)
    ans[0] += 1
print(ans[0], '\n', ' '.join([str(x) for x in ans[1:]]))
-------------- alternate
n = int(input())
s = set()
k = 0
nt = 0

while n not in s:
    nt += 1
    if n - nt > nt:
        s.add(nt)
        n -= nt
    else:
        s.add(n)

print(len(s), '\n', ' '.join([str(x) for x in sorted(list(s))]))

---------- alternate
def calc_n_from_S(S):
    spisok = []
    from math import sqrt
    d_sqrt = int(sqrt(1+8*S))
    n = (-1+d_sqrt)//2
    summa = int(n/2*(n+1))
    raznost = S-summa
    if raznost == 0:
        spisok = [i for i in range(1, n+1)]
    elif raznost > n:
        spisok = [i for i in range(1, n+1)] + [raznost]
    elif raznost > 0:
        spisok = [i for i in range(1, n)] + [n+raznost]
    return spisok

S_n = int(input())
k_list = calc_n_from_S(S_n)
print(len(k_list))
print(*k_list, sep=' ')
----------- alternate
print(*k_list)
------------- alternate
n = int(input())
i = 1
numbers = []
while n > 2*i:
    n -= i
    numbers.append(i)
    i += 1

numbers.append(n)
print(i)
print(*numbers, sep=' ')
------------ alternate
n = int(input())
i = 1
numbers = []
while n > 0:
    if n - i >= 0:
        n -= i
        numbers.append(i)
        i += 1
    else:
        numbers[-1] += n
        break

print(len(numbers))
print(*numbers, sep=' ')


"""

"""
Теоретическая задача для самостоятельной проверки: сдача минимальным количеством монет

Постройте жадный алгоритм, который получает на вход натуральное число nn и за время O(n)O(n) находит минимальное число монет номиналом 
1 копейка, 5 копеек, 10 копеек и 25 копеек, с помощью которых можно выдать сдачу в nn копеек. 
(Как всегда, нужно описать алгоритм, доказать его корректность и оценку на время работы. 
Приводить псевдокод нужно только в том случае, если вам кажется, что он поможет читателю лучше понять ваш алгоритм.)

Приведите пример номиналов монет, для которых жадный алгоритм построит неоптимальное решение. 
В множество номиналов должна входить монета номиналом 1 копейка, чтобы любую сумму nn можно было разменять этими монетами.

У меня получился алгоритм надежным шагом которого является деление числа n на максимальный номинал, 
взятие целой части от получившегося значения(кол-во монет данного номинала) и переход к следующему номиналу меньшего
 достоинства с n = n - int(n/i)*i, где i max номинал. То есть один проход по списку номиналов до момента пока n не равно 0.

Время работы этого алгоритма, как мне кажется, будет меньше чем O(n).  Придумать пример с неоптимальным решением у меня не получилось.

P.S. Если я правильно понял задачу) Видимо это тривиальная задача раз тут нет ни одного комментария )
"""


"""
Задача на программирование: кодирование Хаффмана
По данной непустой строке ss длины не более 104104, состоящей из строчных букв латинского алфавита, постройте оптимальный беспрефиксный код. 
В первой строке выведите количество различных букв kk, встречающихся в строке, и размер получившейся закодированной строки. 
В следующих kk строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0
Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
w = input()
f={}
for i in w:
	if i in f:
		f[i]+=1
	else:
		f[i]=1
#print(f)
d=sorted(f.items(), key=lambda x: (x[1]))
#print(d)
n=len(d)
h=[] #(symbol,freq,ordernum?,flag?) =>? (symbol,freq,id,pid,str)
def insert(a,s,i,pid,str):
	h.append((a,s,i,pid,str))
for i in range(1,n+1,1):
	insert(d[i-1][0],d[i-1][1],i-1,-1,'')
#print(h)
def extractMin():
	i=0
	min=999999
	for j in range(len(h)):
		if h[j][1]<min and h[j][3]==-1:
			min = h[j][1]
			i = j
	return(i,h[i][2],min,h[i][4])
for k in range(n,2*n-1,1):
	i,id,q,s = extractMin()
	h[i]=(h[i][0],q,id,k,s+'0')
	j,id,l,s = extractMin()
	h[j]=(h[j][0],l,id,k,s+'1')
	insert('',q+l,k,-1,'')
if len(h)==1:
	h[0]=(h[0][0],h[0][1],h[0][2],h[0][3],'0')
#print(h)
def gatherCode(symb,id,s):
	print(symb,id,s)
	for i in range(len(h)):
		if h[i][3]==id:
			if h[i][0]==symb:
				return s+(h[i][4] if h[i][4]!='' else '0')
			else:
				if h[i][0]=='':
					if id!=-1:
						return gatherCode(symb,h[i][2],s + h[i][4])
					else:
						return gatherCode(symb,h[i][2],s)
def gatherCode2(symb):
	s=''
	for i in range(len(h)):
		if h[i][0]==symb:
			id=h[i][2]
	while id!=-1:
		for i in range(len(h)):
			if h[i][2]==id:
				s=h[i][4]+s
				id=h[i][3]
				break
	return s
l=''
for i in w:
	l+=gatherCode2(i)#gatherCode(i,-1,'')
print(len(f),len(l))
for i in f:
	print(i+':',gatherCode2(i))#gatherCode(i,-1,'')
for i in w:
	print(gatherCode2(i),end='')#gatherCode(i,-1,'')
	
------- alternate
# put your python code here
from collections import Counter, OrderedDict

s = input()
c = Counter(s)
cc = list(c)
free = []
d1 = c.most_common()


while d1:
    if len(d1) > 1:
        m1 = d1.pop()
        m2 = d1.pop()
        free.append((m1[0], m1[0] + m2[0]))
        free.append((m2[0], m1[0] + m2[0]))
        c = Counter(dict(d1)) + Counter({m1[0] + m2[0]: m1[1] + m2[1]})
        d1 = c.most_common()
    else:
        m1 = d1.pop()
        free.append((m1[0], None))

d = dict()
ft = [x[0] for x in free]

for x in cc:
    i = ft.index(x)
    d[x] = ''
    while free[i][1] is not None:
        d[x] += str(i % 2)
        i = ft.index(free[i][1])
    if not d[x]:
        d[x] = '0'        

for x in d:
    d[x] = d[x][-1::-1]
ou = []
for x in s:
    ou.append(d[x])
u = ''.join(ou)
print(len(d), len(u))
for x in d:
    print('{}: {}'.format(x, d[x]))
print(u)


---- alternate
def get_tree(string):
    from heapq import heappop, heappush
    ss = set(string)
    heap = []
    for c in ss:
        heappush(heap, (string.count(c), c, None, None))
    while len(heap)>1:
        root_1 = heappop(heap)
        root_2 = heappop(heap)
        heappush(heap, (root_1[0]+root_2[0], "\0", root_1, root_2))
    return heap
def get_table(tupl, code, dict_):
    ch = tupl[1]
    left = tupl[2]
    right = tupl[3]
    if left:
        get_table(left, code+"1", dict_)
    if right:
        get_table(right, code+"0", dict_)
    if ch!="\0":
        dict_[ch] = code
def get_coded_string(s, slovar):
    ret = ''
    for c in s:
        ret += slovar.get(c, '')
    return ret

s = input()
if len(set(s))==1:
    d = {s[0]: '0'}
else:
    h = get_tree(s)
    d = {}
    get_table(h[0], "", d)
slovo = get_coded_string(s, d)
print(len(d), len(slovo))
for key, value in d.items():
    print(key, value, sep=": ")
print(slovo)

---------- alternate

class Node:
    def __init__(self, name, left_child=None, right_child=None, parent=None, weight=0):
        self.name = name
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent
        self.weight = weight
        
    def way(self):
        parent = self.parent
        lst = []
        while parent != None: 
            lst.append(parent)
            parent = parent.parent
        return lst
        
def sortkey(key):
    return tree[key][0]

s = input()
if len(s) ==1:
    print(1, 1)
    print(s,': ',0,sep='')
    print(0)
else:
    alphabet = {}
    for letter in s:
        if letter in alphabet:
            alphabet[letter] += 1
        else:
            alphabet[letter] = 1
    if len(alphabet) == 1:
        print(1, len(s))
        print(s[0],': ',0,sep='')
        for t in range (len(s)):
            print(0,sep='',end='')
    else:
        tree = {}
        table = {}
        i = 1
        for key in alphabet:
            tree[i] = [alphabet[key]]
            table[key] = i
            i += 1
        heap = list(tree.keys())
        heap.sort(key=sortkey)
        while len(heap) > 1:
            item0 = heap.pop(0)
            item1 = heap.pop(0)
            tree[i] = [tree[item0][0] + tree[item1][0], item0, item1]
            heap.append(i) 
            heap.sort(key=sortkey)
            i += 1
        for key in tree:
            tree[key].pop(0)
        tree2={}
        for leaf in tree:
            if len(tree[leaf]) == 0:
                tree2[leaf] = Node(name=leaf)
            else:
                tree2[leaf] = Node(name=leaf,left_child=tree[leaf][0],right_child=tree[leaf][1])
            tree2[leaf].parent = [key for key in tree if leaf in tree[key]]
        for key in tree2:
            try:
                if tree2[key].parent == []:
                    tree2[key].parent = None
                else:
                    tree2[key].parent = tree2[tree2[key].parent[0]]
            except IndexError:
                pass
        for key in tree2:
            try:
                tree2[key].left_child = tree2[tree2[key].left_child]
                tree2[key].right_child = tree2[tree2[key].right_child]
            except KeyError:
                pass
        code = {}
        for letter in table:
            slf = tree2[table[letter]]
            wayy = slf.way()
            wayy.reverse()
            wayy.append(slf)
            u = ''
            for i in range(len(wayy)-1):
                if wayy[i+1] == wayy[i].left_child:
                    u += '0'
                elif wayy[i+1] == wayy[i].right_child:
                    u += '1'
            code.update({letter:u})
        s1 = ''
        for char in s:
            s1 += code[char]
        print(len(code), len(s1))
        for key in sorted(code):
            print(key,': ',code[key],sep='')
        print(s1)
------ alternate
from collections import Counter
import heapq
from operator import itemgetter

st = input()
heap = []
c = Counter(st)
frequencies = c.most_common()
for f in frequencies:
    v = (f[1], f[0])
    heapq.heappush(heap, v)

tree = {}
while len(heap) > 1:
    v1 = heapq.heappop(heap)
    v2 = heapq.heappop(heap)
    priority = v1[0] + v2[0]
    value = v1[1] + v2[1]
    heapq.heappush(heap, (priority, value))
    tree[value] = (v1[1], v2[1])


root = heapq.heappop(heap)[1]
q = [(root, '')]
if len(tree) == 0:
    tree[root] = None
    q = [(root, '0')]

code_table = {}
while len(q):
    next_key, prefix_code = q.pop()
    next = tree.get(next_key, None)
    if next:
        q.append((next[0], prefix_code + '0'))
        q.append((next[1], prefix_code + '1'))
    else:
        code_table[next_key] = prefix_code

encoded = ''
for ch in st:
    encoded += code_table[ch]

print(len(code_table), len(encoded))
for ch, code in sorted(list(code_table.items()),key=itemgetter(0)):
    print(ch + ':', code)

print(encoded)


"""

"""
Задача на программирование: декодирование Хаффмана
Восстановите строку по её коду и беспрефиксному коду символов. 
В первой строке входного файла заданы два целых числа kk и ll через пробел — количество различных букв, встречающихся в строке, 
и размер получившейся закодированной строки, соответственно. 
В следующих kk строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого. 
Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз. 
Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный размер.
В первой строке выходного файла выведите строку ss. Она должна состоять из строчных букв латинского алфавита. 
Гарантируется, что длина правильного ответа не превосходит 104104 символов.

Sample Input 1:
1 1
a: 0
0
Sample Output 1:
a
Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:
abacabad


n,m = map(int, input().split())
d={}
for i in range(n):
	l,c = input().split()
	d[c]=l[0]
#print(d)
w=input()
wd=''
while len(w)>0:
	for x in d:
		if w.startswith(x):
			wd+=d[x]
			w=w[len(x):]
			break
print(wd)


--------- alternate
# put your python code here
from heapq import *

a = input().split(' ')
k, l = int(a[0]), int(a[1])

freq = {}

for _ in range(k):
    a = input().split(': ')
    freq[a[1]] = a[0]

enc_str = input()
dec_str = ""
cur_code = ""
for ch in enc_str:
    cur_code += ch
    if freq.get(cur_code):
        dec_str += freq[cur_code]
        cur_code = ""
print(dec_str)
----------- alternate
k, l = input().split()
dic = {}
for _ in range(int(k)):
    l, code = input().split()
    dic[code] = l[:-1]
    
curr = ""
ans = ""
for i in input():
    curr += i
    if curr in dic:
        ans += dic[curr]
        curr = ""
print(ans)
--------------- alternate
k, l = map(int, input().split())
dic = {}
for _ in range(k):
    key, code = input().split(':')
    dic[key] = code.strip()
s = input()
while len(s) > 0:
    for key in dic:
        if s.startswith(dic[key]):
            print(key, end='', sep='')
            s = s[len(dic[key]):]
--------------- alternate
import sys
lines = [line.rstrip() for line in sys.stdin.readlines()]
table = {}
for line in lines[1:-1]:
    letter, code = line.split(': ')
    table[code] = letter

word = ''
buff = ''
for ch in lines[-1]:
    buff += ch
    letter = table.get(buff, None)
    if letter:
        buff = ''
        word += letter

print(word)
----------- alternate

"""
"""
Теоретическая задача для самостоятельной проверки: свойство кода Хаффмана
Докажите, что если частоты всех символов меньше 1/31/3 (другими словами, каждый символ в исходную строку ss входит строго меньше |s|/3|s|/3 раз), 
то коды всех символов в коде Хаффмана будут длиннее одного бита.
"""



"""
Задача на программирование: очередь с приоритетами



Первая строка входа содержит число операций 1≤n≤1051≤n≤105. Каждая из последующих nn строк задают операцию одного из следующих двух типов:

InsertInsert xx, где 0≤x≤1090≤x≤109 — целое число;
ExtractMaxExtractMax.
Первая операция добавляет число xx в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:
200
500


k=[]

def SwimUP():
	i = len(k)
	if i > 1:
		i -= 1
		while ((i > 0) and (k[i//2] < k[i])):
			t = k[i//2]
			k[i//2] = k[i]
			k[i] = t
			i = i//2

def getmax(i,x):
	if 2*i+1>x and 2*i>x:
		return 0
	else:
		if 2*i+1>x:
			return 2*i
		else:
			return 2*i if k[2*i]>k[2*i+1] else 2*i+1

def SwimDown(x):
	i = 0
	#print('shiftdown',i,k,x)
	#y = getmax(i,x-1)
	#print(k,i,y,x-1)
	#while y>0 and k[i]<k[y]:
	#	#print('ki<kj',k,i,y,k[i],k[y])
	#	t = k[i]
	#	k[i] = k[y]
	#	k[y] = t
	#	i+=1
	#	y = getmax(i,x-1)
	#print('end shiftdown')
	while 2*i<=x-1:
		j=i
		if k[2*i]>k[j]:
			j = 2*i
		if 2*i+1<=x-1 and k[2*i+1]>k[j]:
			j=2*i+1
		if j==i:
			break
		t=k[i]
		k[i]=k[j]
		k[j]=t
		i=j
def Insert(a):
	k.append(a)
	SwimUP()
	#print(k)

def ExtractMax(x):
	t = k[0]
	k[0] = k[x-1]
	#print(k)
	k.pop(x-1)
	#print(k)
	SwimDown(x-1)
	return t

n = int(input())
for i in range(n):
	op = input()
	#print(op)
	if op[0] == 'I':
		Insert(int(op.split()[1]))
	else:
		print(ExtractMax(len(k)))
	#print(k)
	
------------- alternate
class MakeHeap():
    
    def __init__(self):
        self.heap = []

    def shift_up(self):
        i = len(self.heap) - 1
        while self.heap[i] > self.heap[(i-1)//2] and i > 0:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def shift_down(self):
        i = 1
        try:
            while len(self.heap) >= 2 * i:
                if self.heap[2*i-1] >= self.heap[2*i] and self.heap[2*i-1] > self.heap[i-1]:
                    self.heap[2*i-1], self.heap[i-1] = self.heap[i-1], self.heap[2*i-1]
                    i = 2 * i
                elif self.heap[2*i] > self.heap[2*i-1] and self.heap[2*i] > self.heap[i-1]:
                    self.heap[2*i], self.heap[i-1] = self.heap[i-1], self.heap[2*i]
                    i = 2 * i + 1
                else:
                    break
        except IndexError:
            if len(self.heap) == 2 * i:
                if self.heap[2*i-1] > self.heap[i-1]:
                    self.heap[2*i-1], self.heap[i-1] = self.heap[i-1], self.heap[2*i-1]
        
    def insert_node(self, node):
        if len(self.heap) == 0:
            self.heap.append(node)
        else:
            self.heap.append(node)
            self.shift_up()

    def extract_max(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            max_node = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.shift_down()
            return max_node


H = MakeHeap()

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'Insert':
        H.insert_node(int(command[1]))
    else:
        print(H.extract_max())
		
------------ alternate
# put your python code here
import heapq
ml = []
heapq.heapify(ml)
n = int(input())
for _ in range(n):
    a = input()
    try:
        c, d = a.split()
        heapq.heappush(ml, -int(d))
    except ValueError:
        c = a
        print(-heapq.heappop(ml))
--------- alternate
import heapq
import sys

input()
h = []
for line in sys.stdin.readlines():
    if 'Insert' in line:
        val = -int(line.split()[1])
        heapq.heappush(h, val)
    elif 'ExtractMax' in line:
        print(-heapq.heappop(h))
"""


"""
Ввод и вывод массива целых чисел разделённых пробелами:

a = list(int(i) for i in input().split())
print(" ".join(map(str, a)))
Если нужно читать много пар чисел, как в этой задаче, то просто:

A = []
for i in range(n):
  a, b = (int(i) for i in input().split())
  A.append((a, b))﻿
  
--------------
Чтобы понять, как работает трюк с reader, нужно узнать про выражения-генераторы (generator expressions) и синтаксис распаковки. 

В вашем примере можно поступить так:

reader = (tuple(map(int, line.split())) for line in input)
n, capacity = next(reader)
[vals_n_weights] = reader  # распакуем единственное значение
или так:

reader = (tuple(map(int, line.split())) for line in input)
(n, capacity), vals_n_weights = reader
-----------------
-- непрерывный рюкзак
import sys

def fractional_knapsack(capacity, values_and_weights):
	order = [(v / w, w) for v,w in values_and_weights]
	order.sort(reverse=True)
	
	acc = 0
	for v_per_w, w in order:
		if w<capacity:
			acc += v_per_w*w
			capacity -= w
		else:
			acc += v_per_w * capacity
			break
	
	return 0

def main():
	reader = (tuple(map(int, line.split())) for line in sys.stdin)
	n,capacity = next(reader)
	values_and_weights = list(reader)
	assert len(values_and_weights) == n
	opt_value = fractional_knapsack(capacity, values_and_weights)
	print("{:.3f}".format(opt_value))
	
if __name__ = "__main__":
	main()
	
------ через двоичную кучу
import heapq
import sys

def fractional_knapsack(capacity, values_and_weights):
	order = [(-v / w, w) for v,w in values_and_weights]
	heapq.heapify(order)
	
	acc = 0
	while order and capacity:
		v_per_w, w = heap.heappop(order)
		can_take = min(w,capacity)
		acc -= v_per_w*can_take
		capacity -= can_take
	
	return 0

def main():
	reader = (tuple(map(int, line.split())) for line in sys.stdin)
	n,capacity = next(reader)
	values_and_weights = list(reader)
	assert len(values_and_weights) == n
	opt_value = fractional_knapsack(capacity, values_and_weights)
	print("{:.3f}".format(opt_value))
	

def test():
	assert fractional_knapsack(0, [(60,20)]) == 0.0
	assert fractional_knapsack(25,[(60,20)]) == 60.0
	assert fractional_knapsack(25, [(60,20), (0,100)]) == 60.0
	assert fractional_knapsack(25, [(60,20),(50,50)] == 60.0 + 5.0
	
	assert fractional_knapsack(50, [(60,20),(100,50),(120,30)] == 180.0

	from random import randint
	from timing import timed
	for attempt in range(100):
		n = randint(1,1000)
		capacity = randint(0,2*10**6)
		values_and_weights = []
		for i in range(n):
			values_and_weights.append((randint(0,2*10**6), randint(1,2*10**6)))
		
		t.timed(fractional_knapsack, capacity, values_and_weights)
		assert t < 5
	
if __name__ = "__main__":
	#main()
	test()
"""

"""
Коды Хаффмана
----------

from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ["left", "right"])):
	def walk(self, code, acc):
		self.left.walk(code, acc + "0")
		self.right.walk(code, acc + "1")
		
class Leaf(namedtuple("Leaf", ["char"])):
	def walk(self, code, acc):
		code[self.char] = acc or "0"

def huffman_encode(s):
	h = []
	for ch, freq in Counter(s).items():
		h.append((freq, len(h), Leaf(ch)))

	heapq.heapify(h)
	
	count = len(h)
	while len(h) > 1:
		freq1, _count1, left = heapq.heappop(h)
		freq2, _count2, right = heapq.heappop(h)
		heapq.heappush(h, (freq1 + freq2, count, Node(left,right)))
		count += 1
	
	code = {}
	if h:
		[(_freq, _count, root)] = h
		root.walk(code, "")
	return code

def main():
	s = input()
	code = huffman_encode(s)
	encoded = "".join(code[ch] for ch in s)
	print(len(code), len(encoded))
	for ch in sorted(code):
		print("{}: {}".format(ch, code[ch]))
	print(encoded)
	
def test(n_iter=100):
	import random
	import string
	
		for i in range(n_iter):
			length= random.randint(0,32)
			s = "".join(random.choice(string.ascii_letters) for _ range(length))
			code = huffman_encode(s)
			encoded = "".join(code[ch[ for ch in s)
			assert hiffman_decode(encoded, code) == s
	
if __name__=="__main__":
	#main()
	test()
	
"""

"""
---------------------------------------------------- экзамен -------------------------------------------------------------------
По данным двум числам 1≤a,b≤2*10^9 найдите наименьшее натуральное число mm, которое делится и на aa, и на bb.

Sample Input:
18 35
Sample Output:
630

#x, y = sorted(map(int, input().split()))
#if y%x==0:
#	print(y)
#else:
#	xx, yy = x, y
#	while x:    
#	    y,  x = x, y % x
#	print(int(xx*yy/y))
a,b = map(int,input().split())
m = a*b
while a != 0 and b != 0:
	if a > b:
		a %= b
	else:
		b %= a
print(m // (a+b))
"""

"""
По данным числам 1≤n≤301≤n≤30 и 1≤w≤1091≤w≤109 и набору чисел 1≤v1,…,vn≤1091≤v1,…,vn≤109 найдите минимальное число kk, 
для которого число ww можно представить как сумму kk чисел из набора {v1,…,vn}{v1,…,vn}. 
Каждое число из набора можно использовать сколько угодно раз. 
Известно, что в наборе есть единица и что для любой пары чисел из набора одно из них делится на другое. 
Гарантируется, что в оптимальном ответе число слагаемых не превосходит 104104.

Выведите число kk и сами слагаемые.

Sample Input:
4 90 1 2 10 50
Sample Output:
5 50 10 10 10 10

x = [int(x) for x in input().split()]
n,w = x[0],x[1]
x.pop(0)
x.pop(0)
#print(n,w,x)
x.sort(reverse=True)
#print(x)
s=[]
while w and x:
	if x[0]<=w:
		s.append(x[0])
		w -= x[0]
	else:
		x.pop(0)
print(len(s)," ".join(map(str,s)))

"""


"""
В первой строке входа дано целое число 2≤n≤2⋅1052≤n≤2⋅105, во второй — последовательность целых чисел0≤a1,a2,…,an≤1050≤a1,a2,…,an≤105. 
Выведите максимальное попарное произведение двух элементов последовательности, то есть max1≤i≠j≤naiajmax1≤i≠j≤naiaj.

Sample Input:
3
1 2 3
Sample Output:
6

n = int(input())
x = [int(x) for x in input().split()]
x.sort(reverse=True)
print(x[0]*x[1])
"""

"""
В первой строке входа дано целое число 3≤n≤2⋅1053≤n≤2⋅105, во второй — последовательность целых чисел 0≤a1,a2,…,an≤1050≤a1,a2,…,an≤105. 
Выведите максимальное произведение трех элементов последовательности, то есть max1≤i<j<k≤naiajakmax1≤i<j<k≤naiajak.

Sample Input:
3
1 2 3
Sample Output:
6

n = int(input())
x = [int(x) for x in input().split()]
x.sort(reverse=True)
print(x[0]*x[1]*x[2])
"""

"""
Дано две строки TT (длиной до 103103) и PP (длиной до 105105). 

Подсчитайте количество точных вхождений второй строки в первую.

Sample Input:
GCGCG
GCG
Sample Output:
2

import re
t = input()
p = input()
patern_p = '(?=(%s))' %  re.escape(p)
print(len(re.findall(patern_p, t)))
------------ alternate
import re
t = input()
p = input()
patern_p = '(?=('+ p +'))'
print(len(re.findall(patern_p, t)))
"""

"""
В первой строке входа дано целое число 3≤n≤2⋅1053≤n≤2⋅105, во второй — последовательность целых чисел 0≤a1,a2,…,an≤1050≤a1,a2,…,an≤105.

Выведите числа массива, соответствующего мин-куче по входным данным.

Sample Input:
7
3 8 4 9 7 5 6
Sample Output:
3 7 4 9 8 5 6


import heapq
k = []
heapq.heapify(k)
n = int(input())
x = [int(x) for x in input().split()]
#print(x)
for i in range(n):
	heapq.heappush(k, x[i])
print(" ".join(map(str, k)))
"""

"""
Удалить максимум из H 	O(log(n))
Увеличить значение в L 	O(n)
Вставить значение в H 	O(log(n))
Удаление из L 			O(1)
Вставить значение в L 	O(n)
Увеличить значение в H 	O(log(n))
"""

http://younglinux.info/book/export/html/60
