"""
Вы анализируете эмоциональный окрас слов. На первой строчке подаётся числа n и m. В следующих n строках подаётся некоторое слово и его целочисленный окрас. Вам необходимо вывести m слов с максимальным окрасом (в любом порядке). Для некоторых слов может подаваться несколько разных значений окраса, надо выбирать максимальное.

Sample Input:

5 3
cool 0
no -10
apple 5
cool 10
school -20

Sample Output:

cool 10
apple 5
no -10
"""

n,m=map(int, input().split())
d={}
for i in range(n):
	w,x=input().split()
	if w in d:
		if int(x) > d[w]:
			d[w]=int(x)
	else:
		d[w]=int(x)
c=0
for i in sorted(d, key=d.__getitem__, reverse=True):
	if c<m:
		print(i,d[i])
		c+=1


"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "00".
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен количеству различных элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1:
1 2 1
1 3 3
1 2 0
00
Sample Output 1:
2 3 4
2 3 3
3 4 3
Sample Input 2:
1
2
1
1
00
Sample Output 2:
2
2
2
1
"""
s=input()
b=[]
c=[]
while s!='00':
	b.append([int(i) for i in s.split()])
	c.append([int(i) for i in s.split()])
	s=input()
for i in range(len(b)):
	for j in range(len(b[i])):
		if (i==(len(b)-1)) and (j!=(len(b[i])-1)):
			c[i][j]=len(set([b[i-1][j],b[0][j],b[i][j-1],b[i][j+1]]))
		elif (i!=(len(b)-1)) and (j==(len(b[i])-1)):
			c[i][j]=len(set([b[i-1][j],b[i+1][j],b[i][j-1],b[i][0]]))
		elif (i==(len(b)-1)) and (j==(len(b[i])-1)):
			c[i][j]=len(set([b[i-1][j],b[0][j],b[i][j-1],b[i][0]]))
		else:
			c[i][j]=len(set([b[i-1][j],b[i+1][j],b[i][j-1],b[i][j+1]]))
for i in c:
	for j in i:
		print(j,end=' ')
	print()

"""
Вам нужно написать класс ConcatReverse, который можно создать либо из строки
ConcatReverse('abcd')
либо из двух других объектов типа ConcatReverse:
a = ConcatReverse('abc')
b = ConcatReverse('def')
c = ConcatReverse(a, b)
Так класс должен иметь метод evaluate, который переворачивает строку в первом случае, а во втором случае склеивает результаты вызовов a.evaluate() и b.evaluate() и затем переворачивает результат.
Ваш код должен выглядеть следующим образом:
class ConcatReverse:
    def __init__(self, *args):
        # Создать объект
    def evaluate(self):
        # Вычислить строку
К примеру:
a = ConcatReverse('abc')
print(a.evaluate()) # 'cba'
b = ConcatReverse('def') => print(b.evaluate)=fed
c = ConcatReverse(a, b)
print(c.evaluate()) # 'defabc' => cbafed => defabc
print(a.evaluate()) # 'cba'
"""
class ConcatReverse:
	def __init__(self, *args):
		self.lst=[]
		self.s=''
		self.type=0
		#print(type(args))
		#if not isinstance(args[0], ConcatReverse): #isinstance('a', str)
		if isinstance(args[0], str):
			self.s=args[0]
			self.type=1
		else:
			self.type=2
			for i in args:
				self.lst.append(i)
	def evaluate(self):
		# Вычислить строку
		self.ss=''
		if self.type==1:
			self.ss=self.s
			return self.ss[::-1] #TypeError: 'JuryCR' object is not subscriptable
			#return ''.join(reversed(self.s)) #TypeError: argument to reversed() must be a sequence
		else:
			for i in range(len(self.lst)):
				self.ss+=self.lst[i].evaluate()
			return self.ss[::-1]

"""
Реализуйте класс, представляющий собой структуру данных, которая позволяет осуществлять следующие операции с шарами из пространства ℤk.
add(r, *coords) – добавить точку
Принимает радиус r и k целых чисел, i-е из которых соответствует i-й координате центра шара.
remove(r, *coords) – удалить точку
Принимает то же, что и add. В случае, если шаров с такими радиусом и координатами несколько, удаляется только один из них. В случае, если соответствующих шаров нет, никакой шар не удаляется.
query(*coords) – запросить шары, покрывающие запрашиваемую точку
Принимает k целых чисел a1,…,ak. Шар (r,x) удовлетворяет запросу, если ∑ki=1(ai−xi)2≤r2, где xi - i
-ая координата центра шара. Результатом данной операции является объект-генератор. Последовательность, получаемая в результате итерации по генератору должна содержать ровно один раз каждый добавленный и не удаленный на момент запроса шар, удовлетворяющую запросу. Шары с одинаковыми координатами и радиусами считаются различными.

Формат решения:

class Spheres:
    def __init__(self, k):
        # k -- размерность пространства

    def add(self, r, *coords):
        # добавить шар

    def remove(self, r, *coords):
        # удалить шар

    def query(self, *coords):
        # запросить шары

Пример использования:

spheres = Spheres(2)
spheres.add(2, 1, 1)
spheres.add(1, -2, 1)
print(list(spheres.query(-1, 1))) # [(2, 1, 1), (1, -2, 1)]
print(list(spheres.query(0, 0))) # [(2, 1, 1)]
spheres.add(6, 0, -2)
spheres.remove(1, -2, 1)
print(list(spheres.query(-1, 1))) # [(2, 1, 1), (6, 0, -2)]
"""
class Spheres:
	def __init__(self, k):
	# k -- размерность пространства
		self.d = {}
		self.c = 0
		self.zk = k
		#for i in range(k):
			#self.d[i]=[]
	def add(self, r, *coords):
	# добавить шар
		#self.d[self.c]=[r,coords]
		self.d[self.c]=[r]
		self.d[self.c]+=list(coords)
		self.c+=1
	def remove(self, r, *coords):
	# удалить шар
		def check(a,b):
			#print(a,b)
			if len(a) == len(b):
				for i in range(len(a)):
					if a[i] == b[i]:
						pass
					else:
						return False
				return True
			else:
				return False
		#print(r,coords)
		for x in self.d:
			#print(('remove',self.d[x][0],r,self.d[x][1:],list(coords)))
			if (self.d[x][0]==r) and check(self.d[x][1:],list(coords)):
				#print(x,self.d[x])
				#print(self.d.index(self.d[x]))
				self.d.pop(x)
				break
	def query(self, *coords):
	# запросить шары
		#print(11111, self.d)
		for x in self.d:
			self.s = 0
			#print(x)
			#print(self.d[x])
			#print(self.d[x][0],self.d[x][1])
			for j in range(self.zk):
				#print('a',coords[j],self.d[x][1][j],pow((coords[j] - self.d[x][1][j]),2))
				#self.s += pow((coords[j] - self.d[x][1][j]),2)
				self.s += pow((coords[j] - self.d[x][1:][j]),2)
			#print('b',self.s,(self.d[x][0])^2)
			if self.s <= pow((self.d[x][0]),2):
				yield self.d[x]

spheres = Spheres(2)
spheres.add(2, 1, 1)
spheres.add(1, -2, 1)
#print(spheres.d,spheres.c,spheres.zk)
print(list(spheres.query(-1, 1))) # [(2, 1, 1), (1, -2, 1)]
print(list(spheres.query(0, 0))) # [(2, 1, 1)]
spheres.add(6, 0, -2)
spheres.remove(1, -2, 1)
print(list(spheres.query(-1, 1))) # [(2, 1, 1), (6, 0, -2)]


"""
Вам дана последовательность строк.
Выведите строки, содержащие в скобках текст, который не содержит внутри себя скобок.
Под текстом подразумевается последовательность символов, содержащая хотя бы один символ из группы \w.
Проверку требуемого условия реализуйте с помощью регулярного выражения.

Sample Input:

good (excellent) phrase
good (too bad) phrase
good ((recursive)) phrase
word () is not () in brackets
bad (() recursive) phrase
no brackets here

Sample Output:

good (excellent) phrase
good (too bad) phrase
good ((recursive)) phrase
"""

import sys
import re

for line in sys.stdin:
	line = line.rstrip()
	p = re.compile('\(\w+.(?!\(\))\w+.\)')
	if not (p.search(line) is None):
		print(line)

"""
Вам дана ссылка на HTML документ.
Посчитайте количество живых картинок в нем.

Живой картинкой назовем тег <img ... src="url" ... >, который отображается на странице, в котором url ведет на страницу, при запросе которой сервер вернет сообщение с status code равным 200 и заголовком Content-Type, начинающимся с image (например image/png)

Пример живой картинки
<img src="https://stepic.org/media/attachments/lesson/25669/nya.png">

Sample Input:
https://stepic.org/media/attachments/lesson/25669/sample.html

Sample Output:
2
"""
import requests
import re

c=0
url=input()
#url='https://stepic.org/media/attachments/lesson/25669/sample.html'
res = requests.get(url)
if res.status_code==200:
	#for url_img in re.findall('\<img.+?src=\"(.*)\".*?>',res.text): #\<img.+?src=\"(.*)\".*?>
	#for url_img in re.findall('\<img\s.*src=\"(.*)\">',res.text):#wr2
	#for url_img in re.findall('\<img\s.*src="([^"]+)">',res.text): #wr3\<img\s.*src=\"(.*)\">
	for url_img in re.findall('\<img[^>]*\ssrc="([^"]+)".*?>',res.text):
		res2 = requests.get(url_img)
		if res2.status_code==200:# & (not (re.search(r'^(image)',res2.headers['Content-Type']) is None)):
			if res2.headers['Content-Type'][0:6]=='image/':
				c+=1
print(c)

"""
Два скучающих солдата играют в карточную войну. Их колода состоит ровно из n карт, пронумерованных различными числами от 1 до n. Исходно они делят между собой карты некоторым, возможно, не равным образом.

Правила игры следующие. На каждом ходу происходит сражение. Каждый игрок берет карту с вершины своей стопки и кладет на стол. Тот, у кого значение карты больше, выигрывает в этом сражении, берет обе карты со стола и кладет в низ своей стопки. Точнее говоря, сперва он берет карту противника и кладет в низ своей стопки, затем кладет свою карту в низ своей стопки. Если после какого-то хода стопка одного игрока становится пустой, то он проигрывает, а другой игрок побеждает.

Вам надо подсчитать, сколько будет сражений и кто победит, или сказать, что игра не прекратится.

Входные данные

В первой строке записано единственное целое число n (2 ≤ n ≤ 10) – количество карт.

Во второй строке записано целое число k1 (1 ≤ k1 ≤ n - 1) – количество карт у первого солдата. Затем следует k1 целых
чисел – значения карт первого солдата в порядке сверху вниз.

В третьей строке записано целое число k2 (k1 + k2 = n) – количество карт у второго солдата. Затем следует k2 целых
чисел – значения карт второго солдата сверху вниз.

Все значения карт различны.

Выходные данные

Если кто-то победит в этой игре, выведите 2 целых числа, где первое число обозначает количество сражений в игре, а второе равно 1, если побеждает первый солдат, и 2, если второй.

Если игра не закончится, а будет продолжаться вечно, выведите  -1.

Sample Input 1:
4
2 1 3
2 4 2

Sample Output 1:
6 2

Sample Input 2:
3
1 2
2 1 3

Sample Output 2:
-1
"""
n=int(input())
k1a = [i for i in input().split()]
k1 = k1a[0]
k1a.pop(0)
k2a = [i for i in input().split()]
k2 = k2a[0]
k2a.pop(0)
x=0
while k1a and k2a:
	x += 1
	a, b = k1a.pop(0), k2a.pop(0)
	if int(a) > int(b):
		k1a += [b, a]
	else:
		k2a += [a, b]
	if x == 999999:
		print(-1)
		break
if x != 999999:
	if k1a:
		print(x,1)
	else:
		print(x,2)
"""
Подходящим назовем файл, имеющий расширение .csv с данными в формате CSV внутри.
Интересным назовем подходящий файл, в заголовке данных которого есть атрибут Pet в любом регистре (pet, PET, pEt, ...)
Хорошим назовем интересный файл, в данных которого строк с атрибутом Pet равным Cat меньше чем строк с атрибутом Pet равным Dog (слова pet, cat и dog могут быть в любом регистре).

Вам дана файловая структура. Найдите количество хороших файлов в ней.

Гарантируется, что любой файл с расширением .csv содержит данные в формате CSV.

Пример данных:
sample.zip

Пример ответа:
43

Основные данные:
data.zip

/home/truename/python/
/home/truename/python/sample/
/home/truename/python/data/
"""
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
