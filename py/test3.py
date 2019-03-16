""" 
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, 
чему равно). 
На вход программе передаётся положительное целое число n — столько элементов последовательности должна отобразить программа. 
На выходе ожидается последовательность чисел, записанных через пробел в одну строку. 

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4. 
  
Sample Input: 
7 

Sample Output: 
1 2 2 3 3 3 4 

n=int(input()) 
b=[] 
i=1 
while i<=n: 
        for c in range(i): 
                b.append(i) 
        i+=1 
for i in range(n): 
        print(b[i],end=' ') 
""" 

""" 
Напишите программу, которая считывает список чисел lst из первой строки и число x 
 из второй строки, которая выводит все позиции, на которых встречается число x 
 в переданном списке lst. 

Позиции нумеруются с нуля, если число x 
 не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы). 
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения. 

Sample Input 1: 
5 8 2 7 8 8 2 4 
8 
Sample Output 1: 
1 4 5 

Sample Input 2: 
5 8 2 7 8 8 2 4 
10 
Sample Output 2: 
Отсутствует 

l=[int(i) for i in input().split()] 
n=int(input()) 
b=[] 
for i in range(len(l)): 
        if l[i]==n: 
                b.append(i) 
if len(b)==0: 
        print("Отсутствует") 
else: 
        for i in b: 
                print(i,end=' ') 
""" 
""" 
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, 
заканчивающихся строкой, содержащей только строку "end" (без кавычек) 
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен 
сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). 
У крайних символов соседний элемент находится с противоположной стороны матрицы. 

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению. 

Sample Input 1: 
9 5 3 
0 7 -1 
-5 2 9 
end 

Sample Output 1: 
3 21 22 
10 6 19 
20 16 -1 

Sample Input 2: 
1 
end 

Sample Output 2: 
4 
""" 
""" 
n=int(input()) 
a=[[0 for i in range(n)] for j in range(n)] 
b=[i for i in range(1,n*n+1)] 
print(a) 
k=1 
f=1 
j=0 
r=0 
while k<=n*n: 
        for cc in range(j,n-j): 
                a[r][cc]=k 
        k+=1 
        r+=1 
        for rr in range(r,n): 
                a[rr][cc]=k 
        k+=1 
        c+=1 
        for cc in range(j,n-j): 
                a[r][cc]=k 
        k+=1 
        r+=1 
------------------------------------- 
""" 
""" 
def modify_list(l): 
        for i in range(len(l)): 
                if l[i]%2==1: 
                        l[i]=-1 
        while -1 in l: 
                l.remove(-1) 
        for i in range(len(l)): 
            l[i]=l[i]//2 

lst = [1, 2, 3, 3, 5, 4, 5, 7, 6] 
modify_list(lst) 
print(lst) 
""" 

""" 
Реализуйте программу, которая будет вычислять количество различных объектов в списке. 
Два объекта a и b считаются различными, если a is b равно False. 
Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке. 

Формат ожидаемой программы: 
ans = 0 
for obj in objects: # доступная переменная objects 
    ans += 1 

print(ans) 

Примечание: 
Количеством различных объектов называется максимальный размер множества объектов, в котором любые два объекта являются различными. 

Рассмотрим пример: 
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным 
Тогда все различные объекты являют собой множество {1, 2, 3}﻿. Таким образом, количество различных объектов равно трём. 

objects=input() 
ans = 0 
b=[] 
for obj in objects: 
        if obj not in b: 
                b.append(obj) 
                ans += 1 
print(ans) 
""" 

""" 
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что: 

•y больше или равно x 

•y делится нацело на 5 

Формат того, что ожидается от вас в качестве ответа: 


def closest_mod_5(x): 
    if x % 5 == 0: 
        return x 
    return "I don't know :(" 

def closest_mod_5(x): 
        if x % 5 == 0: 
                return x 
        else: 
                return closest_mod_5(x+1) 
        return "I don't know :(" 
a=int(input()) 
print(closest_mod_5(a)) 
""" 
""" 
def s(a, *vs, b=10): 
   res = a + b 
   for v in vs: 
       res += v 
   return res 
#print(s(b=31, 0)) 
print(s(11, 10, 10)) 
print(s(11, 10, b=10)) 
print(s(5, 5, 5, 5, 1)) 
#print(s(b=31)) 
print(s(11, 10)) 
print(s(21)) 
print(s(11, b=20)) 
print(s(0, 0, 31)) 
""" 
""" 
def getIsSubClass(c1,c2): 
        b=False 
        if c1==c2: 
                return True 
        else: 
                if len(s[c2]['pid'])==0: 
                        return False 
                else: 
                        if c1 in s[c2]['pid']: 
                                #b=b or True 
                                return True 
                        else: 
                                for j in s[c2]['pid']: 
                                        b=b or getIsSubClass(c1,j) 
                                return b 
n=int(input()) 
s={} 
for i in range(n): 
        x=[i for i in input().split()] 
        if ":" in x: 
                s[x[0]]={'pid':x[2:]} 
                for k in x[2:]: 
                        if k not in s: 
                                s[k]={'pid':[]} 
        else: 
                s[x[0]]={'pid':[]} 
#print(s) 
q=int(input()) 
for i in range(q): 
        a,b=input().split() 
        if getIsSubClass(a,b): 
                print('Yes') 
        else: 
                print('No') 
""" 
""" 
Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса. 

Рассмотрим класс Loggable: 



import time 

class Loggable: 
    def log(self, msg): 
        print(str(time.ctime()) + ": " + str(msg)) 

У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение, добавляя при этом текущее время. 


Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента. 




Примечание 
Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он будет содержать метод log﻿, описанный выше. 
""" 
""" 
def getmax(l): 
        d={} 
        for i in l.split(): 
                if i.lower() in d: 
                        d[i.lower()]['cnt']+=1 
                else: 
                        d[i.lower()]={'cnt':1,'wrd':i.lower()} 
        print(d) 
        max=0 
        maxs='' 
        for i in d: 
                if d[i]['cnt']>max: 
                        max=d[i]['cnt'] 
                        maxs=i 
                elif d[i]['cnt']==max and i<maxs: 
                        max=d[i]['cnt'] 
                        maxs=i 
        print(maxs,max) 
testfile = open("test.txt") 
s=testfile.read(); 
getmax(s) 
testfile.close() 
""" 
""" 
def getmarks(l): 
        d={} 
        d['sum']={1:0,2:0,3:0} 
        for line in l: 
                p=line.replace('\n', '').split(';') 
                #print(p) 
                d[p[0]]={1:int(p[1]),2:int(p[2]),3:int(p[3]),'avg':(int(p[1])+int(p[2])+int(p[3]))/3} 
                print(d[p[0]]['avg']) 
                d['sum'][1]+=int(p[1]) 
                d['sum'][2]+=int(p[2]) 
                d['sum'][3]+=int(p[3]) 
        print(d['sum'][1]/(len(d)-1),d['sum'][2]/(len(d)-1),d['sum'][3]/(len(d)-1)) 
testfile = open("test.txt", "r", encoding='utf-8') 
getmarks(testfile) 
testfile.close() 
""" 
""" 
import math 
print(2*math.pi*float(input())) 
""" 
""" 
import sys 
for i in range(1,len(sys.argv)): 
    print(sys.argv[i],end=' ') 
""" 
""" 
n=int(input()) 
d={} 
for i in range(n): 
        x=input().split(';') 
        if x[0] in d: 
                d[x[0]]['cnt']+=1 
                d[x[0]]['w']+=int(int(x[1])>int(x[3])) 
                d[x[0]]['f']+=int(int(x[1])<int(x[3])) 
                d[x[0]]['o']+=int(int(x[1])==int(x[3])) 
        else: 
                d[x[0]]={'cnt':1,'w': int(int(x[1])>int(x[3])),'f': int(int(x[1])<int(x[3])),'o':int(int(x[1])==int(x[3]))} 
        if x[2] in d: 
                d[x[2]]['cnt']+=1 
                d[x[2]]['w']+=int(int(x[3])>int(x[1])) 
                d[x[2]]['f']+=int(int(x[3])<int(x[1])) 
                d[x[2]]['o']+=int(int(x[3])==int(x[1])) 
        else: 
                d[x[2]]={'cnt':1,'w': int(int(x[3])>int(x[1])),'f': int(int(x[3])<int(x[1])),'o':int(int(x[3])==int(x[1]))} 
for i in d: 
        print(i+':'+str(d[i]['cnt']),d[i]['w'],d[i]['o'],d[i]['f'],(d[i]['w']*3+d[i]['o'])) 
""" 
""" 
s0=[i for i in input()] 
s1=[i for i in input()] 
d={} 
for i in range(len(s0)): 
        d[s0[i]]=s1[i] 
for i in input(): 
        print(d[i],end='') 
print() 
for i in input(): 
        for j in d: 
                if i==d[j]: 
                        print(j,end='') 
""" 
""" 
n=int(input()) 
d=[] 
for i in range(n): 
        d.append(input().lower()) 
#t=[] 
e=[] 
n=int(input()) 
for i in range(n): 
        #t.append(input()) 
        for x in input().split(): 
                if (not x.lower() in d) and (not x.lower() in e): 
                        e.append(x.lower()) 
for i in e: 
        print(i) 
""" 
""" 
n=int(input()) 
x=0 
y=0 
for i in range(n): 
        p=input().split() 
        if p[0]=='север': 
                y+=int(p[1]) 
        elif p[0]=='юг': 
                y-=int(p[1]) 
        elif p[0]=='восток': 
                x+=int(p[1]) 
        else: 
                x-=int(p[1]) 
print(x,y) 
""" 
""" 
def getstat(l): 
        d={} 
        for line in l: 
                p=line.replace('\n', '').split() 
                #print(p) 
                if not int(p[0]) in d: 
                        d[int(p[0])]={'s':int(p[2]),'c':1} 
                else: 
                        d[int(p[0])]['s']+=int(p[2]) 
                        d[int(p[0])]['c']+=1 
        print(d) 
        for i in range(1,12): 
                if not i in d: 
                        print(i,'-') 
                else: 
                        print(i,d[i]['s']/d[i]['c']) 
testfile = open("test.txt", "r", encoding='utf-8') 
getstat(testfile) 
testfile.close() 
""" 
""" 
Вашей программе будет доступна функция foo, которая может бросать исключения. 
Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения. 
Пример решения, которое вы должны отправить на проверку. 
try: 
    foo() 
except Exception: 
    print("Exception") 
except BaseException: 
    print("BaseException") 
Подсказка: https://docs.python.org/3/library/exceptions.html#exception-hierarchy 

try: 
    foo() 
except ZeroDivisionError: 
    print("ZeroDivisionError") 
except ArithmeticError: 
    print("ArithmeticError") 
except AssertionError: 
    print("AssertionError") 
""" 
""" 
def getIsSubClass(c1,lst): 
        b=False 
        if c1 in lst: 
                return True 
        else: 
                #print(lst) 
                if len(s[c1]['pid'])==0: 
                        return False 
                else: 
                        for c2 in s[c1]['pid']: 
                                if c2 in lst: 
                                        return True 
                                else: 
                                        b=b or getIsSubClass(c2,lst) 
                        return b 
n=int(input()) 
s={} 
for i in range(n): 
        x=[i for i in input().split()] 
        if ":" in x: 
                s[x[0]]={'pid':x[2:]} 
                for k in x[2:]: 
                        if k not in s: 
                                s[k]={'pid':[]} 
        else: 
                s[x[0]]={'pid':[]} 
#print(s) 
q=int(input()) 
l=[] 
for i in range(q): 
        a=input() 
        if getIsSubClass(a,l): 
                print(a) 
        l.append(a) 
""" 
""" 
try: 
    foo() 
except ZeroDivisionError: 
    print("ZeroDivisionError") 
except ArithmeticError: 
    print("ArithmeticError") 
except AssertionError: 
    print("AssertionError") 
""" 
""" 
class NonPositiveError(Exception): 
        pass 
class PositiveList(list): 
        def append(self,x): 
                if x >= 0: 
                        raise NonPositiveError 
                else: 
                        self.append(x) 
""" 
""" 
import datetime 
y,m,d=[int(i) for i in input().split()] 
dcnt=int(input()) 
date_=(datetime.date(y,m,d)+datetime.timedelta(days=dcnt)) 
#print((datetime.date(y,m,d)+datetime.timedelta(days=dcnt)).strftime("%Y %m %d")) 
print(date_.year,date_.month,date_.day) 
""" 
""" 
from simplecrypt import encrypt, decrypt 

with open("d:\encrypted.bin", "rb") as inp: 
    encrypted = inp.read() 

testfile = open("d:\passwords.txt", "r", encoding='utf-8') 
for line in testfile: 
        try: 
                print(decrypt(line.replace('\n', '').strip(),encrypted)) 
        except Exception: 
                print("Exception") 
        finally: 
                pass 
testfile.close() 
""" 
""" 
class multifilter: 
    def judge_half(pos, neg): 
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg) 
        return pos >= neg 
    def judge_any(pos, neg): 
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1) 
        return pos >= 1 
    def judge_all(pos, neg): 
        # допускает элемент, если его допускают все функции (neg == 0) 
        return neg == 0 
    def __init__(self, iterable, *funcs, judge=judge_any): 
        # iterable - исходная последовательность 
        # funcs - допускающие функции 
        # judge - решающая функция 
        self.iterable = iterable 
        self.judge = judge 
        self.funcs = funcs 
        #pos=len([x for x in iterable for f in funcs if f(x)]) 
    def __iter__(self): 
        # возвращает итератор по результирующей последовательности 
        for x in self.iterable: 
            pos=0 
            neg=0 
            for f in self.funcs: 
                if f(x): 
                    pos+=1 
                else: 
                    neg+=1 
            if self.judge(pos,neg): 
                yield x 
""" 
""" 
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27] 
print(list(filter(lambda x: x % 3 == 0, foo))) 
[18, 9, 24, 12, 27] 


Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя. 
Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел. 
Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1. 

Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2. 

Пример использования:﻿ 
print(list(itertools.takewhile(lambda x : x <= 31, primes()))) 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] 

import math 
def is_prime(a): 
        if a<=1: 
                return False 
        if a%2==0: 
                return False 
        for i in range(3,int(math.sqrt(a))+1,1):         
                if a%i==0: 
                        return False 
        return True 
def primes(): 
    x=2 
    yield 2 
    while True: 
        x+=1 
        if is_prime(x): 
            yield x 
""" 
""" 
d=[] 
with open("dataset_24465_4.txt") as f: 
        for l in f: 
                d.append(l.strip()) 
with open("new2.txt","w") as f: 
        for l in range(len(d)-1,-1,-1): 
                f.write(d[l]+'\n') 
""" 
""" 
import os 
path="main" 
d=[] 
for (path,dirs,files) in os.walk(path): 
        if len(list(filter(lambda file : file[-3:]==".py", files)))>0: 
                if not path in d: 
                        d.append(path) 
with open("dirs.txt","w") as f: 
        for i in sorted(d): 
                #print(i) 
                f.write(i+'\n') 
""" 
""" 
def mod_checker(x, mod=0): 
        return (lambda y: y%x==mod) 
mod_3 = mod_checker(3) 

print(mod_3(3)) # True 
print(mod_3(4)) # False 

mod_3_1 = mod_checker(3, 1) 
print(mod_3_1(4)) # True 
""" 
""" 
s, a, b = [input().strip() for _ in range(3)] 
if a in s: 
        if a in b: 
                print("Impossible") 
        else: 
                cnt = 0 
                while a in s: 
                        cnt += 1 
                        s = s.replace(a,b) 
                print(cnt) 
else: 
        print(0) 
""" 
""" 
s, t = [input().strip() for _ in range(2)] 
cnt = 0 
i = 0 
while i < len(s): 
        if s.find(t,i) > -1: 
                #print(s.find(t,i)) 
                if s.find(t,i) > i: 
                        i = s.find(t,i)+1 
                else: 
                        i += 1 
                cnt += 1 
        else: 
                i += 1 
print(cnt) 
""" 
""" 
import sys 
import re 

for line in sys.stdin: 
        line = line.rstrip() 
        #p = re.compile('(cat(.*)){2,}') 
        #if not p.match(line) is None: 
        #        print(line) 
        p = re.compile('(cat(.*)){2,}') 
        #print(p.search(line)) 
        if not (p.search(line) is None): 
                print(line) 
""" 
""" 
import sys 
import re 

for line in sys.stdin: 
        line = line.rstrip() 
        #p = re.compile('(cat(.*)){2,}') 
        #if not p.match(line) is None: 
        #        print(line) 
        p = re.compile(r'\bcat\b') 
        #print(p.search(line)) 
        if not (p.search(line) is None): 
                print(line) 
""" 
""" 
import sys 
import re 

for line in sys.stdin: 
        line = line.rstrip() 
        if not (re.search(r'z(.{3})z',line) is None): 
                print(line) 
""" 
""" 
import sys 
import re 

for line in sys.stdin: 
        line = line.rstrip() 
        if not (re.search(r'.*\\.*',line) is None): 
                print(line) 
""" 
""" 
>>> p = re.compile(r'(\b\w+)\s+\1') 
>>> p.search('Paris in the the spring').group() 
'the the' 

import sys 
import re 

for line in sys.stdin: 
        line = line.rstrip() 
        if not (re.search(r'\b([a-zA-Z0-9]+)\1\b',line) is None): 
                print(line) 
""" 
""" 
import sys 
import re 
for line in sys.stdin: 
        line = line.rstrip() 
        print(re.sub('(human)','computer',line)) 
""" 
""" 
Вам дана последовательность строк. 
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh". 
Примечание: 
Обратите внимание на параметр count у функции sub﻿. 
Sample Input: 
There’ll be no more "Aaaaaaaaaaaaaaa" 
AaAaAaA AaAaAaA 
Sample Output: 
There’ll be no more "argh" 
argh AaAaAaA 

import sys, re 
for line in sys.stdin: 
        line = line.rstrip() 
        print(re.sub(r'\b([aA]+)\b','argh',line, count = 1)) 
""" 
""" 
import sys, re 
def repl(m): 
        return m.group(2)+m.group(1)+m.group(3) 

for line in sys.stdin: 
        line = line.rstrip() 
        print(re.sub(r'\b(\w)(\w)(\w*)\b',repl,line)) 
""" 
""" 
buzzzzzbasdasdzzzzz -> buzbasdasdz 
import sys, re 
def repl(m): 
        return m.group(1) 

for line in sys.stdin: 
        line = line.rstrip() 
        print(re.sub(r'(\w)\1+',repl,line)) 
""" 
""" 
Sample Input: 
0 
10010 
00101 
01001 
Not a number 
1 1 
0 0 

Sample Output: 
0 
10010 
01001 
""" 
""" 
import sys, re 
def d3(t): 
        multiplier = 1 
        accumulator = 0 
        for bit in t: 
                accumulator = (accumulator + int(bit) * multiplier) % 3 
                multiplier = 3 - multiplier 
        return accumulator == 0 

#print(re.findall(r'\d','0101111')) 
for line in sys.stdin: 
        line = line.rstrip() 
        if not (re.search(r'^([01]+)\Z',line) is None): 
                #print(line) 
                if d3(line): 
                        print(line) 
        #print(re.sub(r'(\w)\1+',repl,line)) 
""" 
""" 
import urllib 

link = "https://stepic.org/media/attachments/lesson/24472/sample0.html" 
try: 
        #f = urllib.urlopen(link) 
        #print(f) 
        #myfile = f.read() 
        #print(myfile) 
        
        req = urllib.request.Request(link) 
        with urllib.request.urlopen(req) as response: 
                the_page = response.read() 
        print(the_page) 
        
        #import requests 
        #f = requests.get(link) 
        #print(f.text) 
except Exception as e: 
        pass 
""" 
""" 
import csv 
d={} 
with open('Crimes.csv') as csvfile: 
        lines = csv.DictReader(csvfile, delimiter=',') 
        for line in lines: 
                if not line['Primary Type'] in d: 
                        d[line['Primary Type']] = 0 
                else: 
                        d[line['Primary Type']] += 1 
#print(d) 
#for w in sorted(d, key=d.get, reverse=True): 
#        print(w, d[w]) 
print(sorted(d, key=d.get, reverse=True)[0]) 
""" 
""" 
import json 

def getIsSubClass(c1,c2): 
        b=False 
        #if c1==c2: 
        #        return True 
        #else: 
        if len(dd[c2]['pid'])==0: 
                return False 
        else: 
                if c1 in dd[c2]['pid']: 
                        return True 
                else: 
                        for j in dd[c2]['pid']: 
                                b=b or getIsSubClass(c1,j) 
                        return b 

d=json.loads(input()) 
dd={} 
for i in d: 
        dd[i['name']]={'pid':i['parents'],'cnt':0} 
for i in dd: 
        for j in dd: 
                if getIsSubClass(i,j): 
                        dd[i]['cnt'] += 1 

for i in sorted(dd): 
        print(i,':',dd[i]['cnt']+1) 
""" 
""" 
http://numbersapi.com/31/math?json=true 
 { 
 "text": "31 is a repdigit in base 5 (111), and base 2 (11111).", 
 "number": 31, 
 "found": true, 
 "type": "math" 
} 
http://numbersapi.com/999/math?json=true 
{ 
 "text": "999 is an unremarkable number.", 
 "number": 999, 
 "found": false, 
 "type": "math" 
} 
""" 
""" 
import urllib.request 
import json 

#link = "http://numbersapi.com/31/math?json=true" 
try: 
        #req = urllib.request.Request(link) 
        #with urllib.request.urlopen(link) as response: 
        #        the_page = response.read() 
        num=int(input()) 
        with urllib.request.urlopen("http://numbersapi.com/"+num+"/math?json=true") as response: 
                the_page = response.read() 
        d=json.loads(the_page) 
        for i in d: 
                if i['found']: 
                        print('Interesting') 
                else: 
                        print('Boring') 
except Exception as e: 
        print(e) 
""" 
""" 
import urllib.request, json 
url = "http://numbersapi.com/31/math?json=true" 
response = urllib.request.urlopen(url) 
data = json.loads(response.read()) 
print(data) 
""" 
""" 
import requests 
import re 

def checkWayBy2Step(url_b, url_e): 
    res = requests.get(url_b) 
    if res.status_code==200: 
        #print(res.text) 
        for url2 in re.findall('\<a\s.*href=\"(.*)\">',res.text): 
            #print(url2) 
            res2 = requests.get(url2) 
            if res2.status_code==200: 
                for url3 in re.findall('\<a\s.*href=\"(.*)\">',res2.text): 
                    if url3 == url_e: 
                        return True 
    return False 

url1='https://stepic.org/media/attachments/lesson/24472/sample0.html'#input() 
url2='https://stepic.org/media/attachments/lesson/24472/sample0.html'#input() 
if checkWayBy2Step(url1,url2): 
    print('Yes') 
else: 
    print('No') 
""" 
""" 
import requests 
import re 

def getUrl(url): 
        try: 
                if (re.search(r'^\.\.',url) is None): 
                        if not (re.search(r'\/\/',url) is None): 
                                return re.findall(r'^(([^:/?#]+):)?(//([^/?#:\"\']*))?([^?#]*)(\?([^#]*))?(#(.*))?',url)[0][3] 
                        else: 
                                return re.findall(r'^(([^:/?#]+):)?(//([^/?#:\"\']*))?([^?#]*)(\?([^#]*))?(#(.*))?',url)[0][4] 
        except Exception: 
                pass 
d = [] 
#ur='https://stepic.org/media/attachments/lesson/24471/03'#input() 
#res = requests.get(ur) 
#if res.status_code == 200: 
#        for url in re.findall('\<a\s.*href=[\"\'](.*)[\"\'\s]+?>',res.text): 
with open('urls.txt') as f: #, "r", "UTF-8" 
        for line in f: 
                #for url in re.findall('\<a\s.*href=[\"\'](.*)[\"\'\s]>',line): 
                #print(line) 
                for url in re.findall('\<a\s.*href=[\"\'](.*)[\"\'\s]>',line): 
                        u = getUrl(url) 
                        if not u is None: 
                                if not u in d: 
                                        d.append(u) 
for i in sorted(d): 
        print(i) 

#d[i] = {'url':getUrl(line)} 
#print(line) 
#with open('urls.txt') as f: 
#for line in f: 
""" 
""" 
def url_path_to_dict(path): 
    pattern = (r'^' 
               r'((?P<schema>.+?)://)?' 
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?' 
               r'(?P<host>.*?)' 
               r'(:(?P<port>\d+?))?' 
               r'(?P<path>/.*?)?' 
               r'(?P<query>[?].*?)?' 
               r'$' 
               ) 
    regex = re.compile(pattern) 
    m = regex.match(path) 
    d = m.groupdict() if m is not None else None 

    return d 

def main(): 
    print url_path_to_dict('http://example.example.com/example/example/example.html') 
""" 

""" 
# correct 
import requests 
import re 

def url_path_to_dict(path): 
    pattern = (r'^' 
               r'((?P<schema>.+?)://)?' 
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?' 
               r'(?P<host>.*?)' 
               r'(:(?P<port>\d+?))?' 
               r'(?P<path>/.*?)?' 
               r'(?P<query>[?].*?)?' 
               r'$' 
               ) 
    regex = re.compile(pattern) 
    m = regex.match(path) 
    d = m.groupdict() if m is not None else None 

    return d 

d = [] 
ur=input() 
res = requests.get(ur) 
if res.status_code == 200: 
    for url in re.findall('\<a\s.*href=[\"\'](.*?)[\"\'\s]+?',res.text): 
        if (re.search(r'^\.\.',url) is None): 
            u = url_path_to_dict(url) 
            if not u['host'] is None: 
                if not u['host'] in d: 
                    d.append(u['host']) 
else: 
        print(res.status_code) 
for i in sorted(d): 
        print(i) 
""" 
""" 
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com 
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе. 
Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе. 
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле. 
Пример запроса к интересному числу: 
http://numbersapi.com/31/math?json=true 
Пример запроса к скучному числу: 
http://numbersapi.com/999/math?json=true 
Пример входного файла: 
31 
999 
1024 
502 
﻿Пример выходного файла: 
Interesting 
Boring 
Interesting 
Boring 
#--------------------------------------------------- 
import requests 
import re 
import json 

try: 
        with open("d:\\_Projects\\_OLD\\input.txt") as f: 
                for line in f: 
                        num=line.strip() 
                        res = requests.get("http://numbersapi.com/"+num+"/math?json=true") 
                        if res.status_code == 200: 
                                d=json.loads(res.text) 
                                with open("d:\\_Projects\\_OLD\\output.txt","a") as ff: 
                                        if d['found']: 
                                                #print('Interesting') 
                                                ff.write('Interesting'+'\n') 
                                        else: 
                                                #print('Boring') 
                                                ff.write('Boring'+'\n') 
except Exception as e: 
        print(e) 
""" 
""" 
В этой задаче вам необходимо воспользоваться API сайта artsy.net 
API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках. 
В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники). 
Вам даны идентификаторы художников в базе Artsy. 
Для каждого идентификатора получите информацию о имени художника и годе рождения. 
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке. 
Работа с API Artsy 
Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа. 
Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы. 
После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python. 
import requests 
import json 
client_id = '...' 
client_secret = '...' 
# инициируем запрос на получение токена 
r = requests.post("https://api.artsy.net/api/tokens/xapp_token", 
                  data={ 
                      "client_id": client_id, 
                      "client_secret": client_secret 
                  }) 
# разбираем ответ сервера 
j = json.loads(r.text) 
# достаем токен 
token = j["token"] 
Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python. 
# создаем заголовок, содержащий наш токен 
headers = {"X-Xapp-Token" : token} 
# инициируем запрос с заголовком 
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers) 
# разбираем ответ сервера 
j = json.loads(r.text) 
Обратите внимание, что для сортировки художников по имени используется параметр sortable_name. 
Пример входных данных: 
4d8b92b34eb68a1b2c0003f4 
537def3c139b21353f0006a6 
4e2ed576477cc70001006f99 
Пример выходных данных: 
Abbott Mary 
Warhol Andy 
Abbas Hamra 
﻿Примечание для пользователей Windows 
При открытии файла для записи на Windows ﻿по ﻿умолчанию ﻿используется кодировка CP1251, в то время как для записи имен на сайте используется кодировка UTF-8, что может привести к ошибке при попытке записать в файл имя с необычными символами. 


import requests 
import json 

client_id = '4cf6100d0975c9763481' 
client_secret = 'd05320f6d690dfabaee6ff7dd7809470' 
r = requests.post("https://api.artsy.net/api/tokens/xapp_token", 
                  data={ 
                      "client_id": client_id, 
                      "client_secret": client_secret 
                  }) 
j = json.loads(r.text) 
token = j["token"] 
headers = {"X-Xapp-Token" : token} 
artists={} 
with open("d:\\_Projects\\_OLD\\input.txt") as f: 
        for line in f: 
                num = line.strip() 
                r = requests.get("https://api.artsy.net/api/artists/"+num, headers=headers) 
                q = json.loads(r.text) 
                #print(q) 
                artists[q['sortable_name'].encode('utf8')]=q['birthday'] 
print(sorted(artists.items(), key=lambda x: (x[1], x[0]))) 
with open("d:\\_Projects\\_OLD\\output.txt","wb") as ff: 
        for i in [v[0] for v in sorted(artists.items(), key=lambda x: (x[1], x[0]))]: 
                ff.write(i+b'\n')#.decode('utf8') 
""" 



""" 
Вам дано описание пирамиды из кубиков в формате XML. 
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿). 
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним. 
Пример: 
<cube color="blue"> 
  <cube color="red"> 
    <cube color="green"> 
    </cube> 
  </cube> 
  <cube color="red"> 
  </cube> 
</cube> 
Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д. 
Ценность цвета равна сумме ценностей всех кубиков этого цвета. 
Выведите через пробел три числа: ценности красного, зеленого и синего цветов. 
Sample Input: 
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube> 
Sample Output: 
4 3 1 

import xml.etree.ElementTree as etree 
def gatherdict(r,lev): 
        if not r.attrib['color'] in d: 
                d[r.attrib['color']] = lev 
        else: 
                d[r.attrib['color']] += lev 
        for c in r: 
                if len(c.attrib['color'])>0: 
                        gatherdict(c, lev + 1) 
d={} 
n=input() 
root = etree.fromstring(n) 
gatherdict(root,1) 
s = '' 
if 'red' in d: 
    s = str(d['red']) 
else: 
    s = '0' 
if 'green' in d: 
    s += ' ' + str(d['green']) 
else: 
    s += ' 0' 
if 'blue' in d: 
    s += ' ' + str(d['blue']) 
else: 
    s += ' 0' 
print(s)
"""

k,n=[int(i) for i in input().split()]
#print(k,n)
if k>=n:
	print(0)
else:
	for k1 in range(k):
		for i in range(n):
			p=[i]
			for j in range(i+k1+1,n):
				#if i ==0 and j == 3:
				#	print(i,j,k1,i+k1+1,p)
				if len(p)<k:
					p.append(j)
				#else:
				#	print(p)
				#	p=[i,j]
			if len(p)==k:
				print(p)


    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

			
import itertools
k,n=[int(i) for i in input().split()]
for p in itertools.combinations(range(n),k):
    print(' '.join(str(x) for x in p))

	
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

		
"""

Лаборатория
Ввести с клавиатуры строку латиницей (1-3 слова). Зашифровать ее с использованием гарантированных алгоритмов шифрования. Сформировать словарь, где в качестве ключа используется название гарантированного алгоритма шифрования, а в качестве значения - результат шифрования в шестнадцатеричном представлении { 'sha1': 'aaf4c…', 'md5', '5d4…',…}.
Итог вывести отдельными операторами вывода в виде пар ключа и значения, отсортированных по возрастанию ключа:
md5 5d414…
sha1 aaf4c…
"""		
import hashlib
s=input()
h={}
h['md5']=(hashlib.md5(s.encode())).hexdigest()
h['sha1']=(hashlib.sha1(s.encode())).hexdigest()
h['sha224']=(hashlib.sha224(s.encode())).hexdigest()
h['sha256']=(hashlib.sha256(s.encode())).hexdigest()
h['sha384']=(hashlib.sha384(s.encode())).hexdigest()
h['sha512']=(hashlib.sha512(s.encode())).hexdigest()
for i in sorted(h):
    print(i,h[i])