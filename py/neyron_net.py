"""
Нейронный сети
"""
"""
https://www.codecogs.com/latex/eqneditor.php
"""
"""
Источники

При создании курса я, конечно, использовал множество различных источников и опирался на опыт некоторых других онлайн-курсов. 
Ниже приведены те из них, которые просто нельзя не упомянуть перед началом нашего курса.  Данный список будет постепенно пополняться.

https://www.coursera.org/learn/machine-learning/ — живая легенда, курс Andrew Ng по машинному обучению. С него началось когда-то моё увлечение этой темой. 
Крайне рекомендую к просмотру и, пользуясь случаем, хочу выразить публично глубокую благодарность его автору.

http://neuralnetworksanddeeplearning.com/ — замечательная онлайн-книга по нейросетям. Я, кстати, потихоньку её перевожу 
(первые главы должны появиться в открытом доступе в начале лета).

https://www.coursera.org/learn/neural-networks﻿ — я уже использовал фразу «живая легенда»  и теперь испытываю сложности, 
поскольку как-то иначе охарактеризовать Джеффри Хинтона (человека, стоящего у истоков современных подходов к обучению нейросетей 
с помощью алгоритма обратного распространения ошибки) сложно. Курс у него получился отличный.

https://ulearn.azurewebsites.net/Course/AIML/ — недавно обнаружил этот курс, приятные и качественные лекции по широкому набору тем. 
Единственный из источников на русском языке.

http://cs231n.github.io/﻿ — прекрасный курс от Стэнфордского университета, чуть более сложный, пожалуй, чем наш.﻿

"""

"""
import numpy as np
print(2*np.eye(3,4) + np.eye(3,4,1))
"""
"""
Основные методы ndarray

Для работы с многомерными массивами в NumPy реализованы самые часто требующиеся операции. 
Некоторые из них (которые особенно часто будут нужны в нашем курсе) мы сейчас покажем.

Форма массива
a.flatten() — превращает массив в одномерный.
a.T или a.transpose(*axes) — транспонирование (или смена порядка осей в случае, 
когда размерность массива больше двух).
a.reshape(shape) — смена формы массива. Массив "распрямляется" и построчно 
заполняется в новую форму.

>>> import random
>>> w = np.array(random.sample(range(1000), 12)) # одномерный массив из 
12 случайных чисел от 1 до 1000
>>> w = w.reshape((2,2,3)) # превратим w в трёхмерную матрицу
>>> print(w)
[[[536 986 744]
  [543 248 544]]

 [[837 235 415]
  [377 141 751]]]
>>> print(w.transpose(0,2,1))
[[[536 543]
  [986 248]
  [744 544]]

 [[837 377]
  [235 141]
  [415 751]]]
 """
"""
Массив, который нужно было создать в предыдущей задаче, хранится в переменной mat. 
Превратите его в вертикальный вектор и напечатайте.
import numpy as np
mat = mat.reshape((12,1))
print(mat)
"""


"""
Основные методы ndarray

Базовые статистики

a.min(axis=None), a.max(axis=None), a.mean(axis=None), a.std(axis=None) —
 минимум, максимум, среднее арифметическое и стандартное отклонение вдоль указанной оси. 
 По умолчанию ось не указана и статистика считается по всему массиву. a.argmin(axis=None),
 a.argmax(axis=None) — индексы минимального и максимального элемента. 
 Пример:
>>> print(v)
[[1 2 3 4]
 [1 2 3 4]
 [1 2 3 4]]
>>> print(v.mean(axis=0))  # вдоль столбцов
[ 1.  2.  3.  4.]
>>> print(v.mean(axis=1))  # вдоль строк
[ 2.5  2.5  2.5]
>>> print(v.mean(axis=None))  # вдоль всего массива
2.5
Чтобы лучше понять, почему говорят «усреднение вдоль оси» — можно нарисовать 
эту матрицу на бумажке и прямыми линиями соединить те элементы, которые сливаются 
в один при усреднении. Чтобы было совсем понятно — можно ещё добавить координатные оси, 
чтобы каждый элемент wijwij оказался над точкой (i,j)(i,j).
a.sum(axis=None), a.prod(axis=None) — сумма и произведение всех элементов вдоль 
указанной оси. a.cumsum(axis=None), a.cumprod(axis=None) — частичные суммы и произведения
 (для (a1,⋯,an)(a1,⋯,an) вектор частичных сумм — это (a1,a1+a2,⋯,a1+⋯+an)(a1,a1+a2,⋯,a1+⋯+an)).
Линейная алгебра
Пакет numpy.linalg содержит большую часть стандартных операций и разложений матриц. 
Некоторые самые популярные функции вынесены в корень пакета NumPy.
a.dot(b) — матричное произведение двух массивов (размерности должны быть согласованы),
linalg.matrix_power(M, n) — возведение матрицы M в степень n,
a.T — транспонирование
linalg.norm(a, ord=None) — норма матрицы a, по умолчанию норма Фробениуса для матриц 
и L2-норма для векторов; подробное описание возможных норм — в справке,
linalg.inv(a) — матрица, обратная к a (если a необратима, выбрасывается LinAlgError; 
псевдообратная считается через linalg.pinv(a))

>>> a = w.dot([1,2,3])
>>> print(a)
[[4740 2671]
 [2552 2912]]
>>> ainv = np.linalg.inv(a)
>>> print(a.dot(ainv))
[[  1.00000000e+00   0.00000000e+00]
 [ -2.22044605e-16   1.00000000e+00]]

Подробные описания с указанием полного списка аргументов, а также описания всех остальных 
функций находятся на сайте проекта NumPy.
"""
"""
print(linalg.inv((np.eye(3,k=0))))
a.dot(a.T)
print(w.sum(axis=None))
6062

print(w.prod(axis=None))
1571962880

print(w.cumsum(axis=None))
[ 428  505 1002 1190 2065 2947 3277 3389 3606 4144 5098 6062]

a=w.dot([1,2,3])

print(a)
[[2073 4584]
 [1205 5338]]

ainv=np.linalg.inv(a)

print(a.dot(ainv))
[[ 1.  0.]
 [ 0.  1.]]
"""
"""
Задача: перемножьте две матрицы!

На вход программе подаются две матрицы, каждая в следующем формате: 
на первой строке два целых положительных числа nn и mm, разделенных пробелом -
 размерность матрицы. В следующей строке находится n⋅mn⋅m целых чисел, разделенных 
 пробелами - элементы матрицы. Подразумевается, что матрица заполняется построчно, 
 то есть первые mm чисел - первый ряд матрицы, числа от m+1m+1 до 2⋅m2⋅m - второй, и т.д.

Напечатайте произведение матриц XYTXYT, если они имеют подходящую форму, или строку 
"matrix shapes do not match", если формы матриц не совпадают должным образом. 

В этот раз мы проделали за вас подготовительную работу по считыванию матриц (когда 
вы начнёте решать, этот код будет уже написан):

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
 Несколько комментариев:

map(f, iterable, …) — встроенная функция языка Python, возвращает результат поэлементного 
применения функции f к элементам последовательности iterable; если f принимает несколько 
аргументов, то на вход должно быть подано соответствующее число последовательностей: 
результатом map(f, x, y, z) будет итератор, возвращающий поочерёдно 
f(x[0], y[0], z[0]), f(x[1], y[1], z[1]), f(x[2], y[2], z[2]) и так далее; 
результат применения f к очередному набору аргументов вычисляется только тогда, 
когда требуется использовать этот результат, но не ранее, подробнее и короче в справке;
np.fromiter создаёт NumPy-массив из итератора, то есть заставляет итератор вычислить 
все доступные значения и сохраняет их в массив;
input() — встроенная функция языка Python, читает одну строку (последовательность 
символов вплоть до символа переноса строки) из входного потока данных и возвращает 
её как строку;
split() — метод класса string, возвращает список слов в строке (здесь слова — 
последовательности символов, разделённые пробельными символами); принимает дополнительные 
аргументы, подробнее в справке.
Sample Input 1:
2 3
8 7 7 14 4 6
4 3
5 5 1 5 2 6 3 3 9 1 4 6
Sample Output 1:
[[ 82  96 108  78]
 [ 96 114 108  66]]
Sample Input 2:
2 3
5 9 9 10 8 9
3 4
6 11 3 5 4 5 3 2 5 8 2 2
Sample Output 2:
matrix shapes do not match


import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

# here goes your solution; X and Y are already defined!
if x_shape[1]==y_shape[1]:
	print(X.dot(Y.T))
else:
	print('matrix shapes do not match')
"""

"""
Как считать данные из файла:

>>> sbux = np.loadtxt("sbux.csv", usecols=(0,1,4), skiprows=1, delimiter=",", 
                      dtype={'names': ('date', 'open', 'close'),
                             'formats': ('datetime64[D]', 'f4', 'f4')})
>>> print(sbux[0:4])
[(datetime.date(2015, 9, 1), 53.0, 57.2599983215332)
 (datetime.date(2015, 8, 3), 58.619998931884766, 54.709999084472656)
 (datetime.date(2015, 7, 1), 53.86000061035156, 57.93000030517578)
 (datetime.date(2015, 6, 1), 51.959999084472656, 53.619998931884766)]
 
Здесь использованы не все параметры функции loadtxt (полный их список можно 
посмотреть в справке). Разберём имеющиеся, так как они являются наиболее часто встречающимися.
"sbux.csv" — имя файла (или сюда же можно передать объект файла, такой пример 
вы увидите в следующей задаче урока), из которого считываются данные.
usecols — список колонок, которые нужно использовать. 
Если параметр не указан, считываются все колонки.
skiprows — количество рядов в начале файла, которые нужно пропустить. 
В нашем случае пропущен ряд заголовков. По умолчанию (если значение параметра 
не указано явно) skiprows = 0.
delimiter — разделитель столбцов в одной строке, в csv-файлах это запятая, 
по умолчанию разделителем является любой пробел (в том числе — знак табуляции).
dtype — словарь из названий колонок (переменных) и типов хранящихся в них значений. 
NumPy использует свою собственную систему типов, и названия именно этих типов нужно указать. 
По умолчанию функция попытается самостоятельно угадать, какому типу принадлежат 
подаваемые на вход значения.
"""
"""
Задача: считайте данные из файла и посчитайте их средние значения.

На вход вашему решению будет подан адрес, по которому расположен csv-файл, 
из которого нужно считать данные. Первая строчка в файле — названия столбцов, 
остальные строки — числовые данные (то есть каждая строка, кроме первой, состоит из 
последовательности вещественных чисел, разделённых запятыми).

Посчитайте и напечатайте вектор из средних значений вдоль столбцов входных данных. 
То есть если файл с входными данными выглядит как

a,b,c,d
1.5,3,4,6
2.5,2,7.5,4
3.5,1,3.5,2
то ответом будет

[ 2.5  2.   5.   4. ]
Как упоминалось на предыдущем шаге, в качестве файла для loadtxt можно передать объект файла. 
Это удобно в таких случаях, как сейчас: когда данные лежат не на вашем компьютере, 
а где-то в сети. Как их скачать из сети? С помощью стандартных библиотек:

>>> from urllib.request import urlopen
>>> f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')

Теперь в f содержится объект файла, который можно передать в loadtxt.

Sample Input:
https://stepic.org/media/attachments/lesson/16462/boston_houses.csv
Sample Output:
[ 22.53280632   3.61352356  11.36363636   0.06916996   0.55469506
   6.28463439   3.79504269]

   
-------------
from urllib.request import urlopen
import numpy as np
filename = input()
f = urlopen(filename)
sbux = np.loadtxt(f, skiprows=1, delimiter=",")
print(sbux.mean(axis=0))
"""

"""
Теперь давайте попробуем применить наши новые матричные формулы — сначала на 
игрушечном примере, который мы рассматривали пару видео назад.
У нас есть набор данных: знания о длине тормозного пути и скорости для трёх автомобилей.
D	V
10	60
7	50
12	75
Напишите через запятую оценки коэффициентов линейной регрессии D на V, 
т.е. β^0, β^1 для модели D=β0+β1V+ε с точностью до трёх знаков после точки.

import numpy as np
import numpy.linalg as linalg

X=np.array([1,60,1,50,1,75])
print(X.reshape(3,2))
[[ 1 60]
 [ 1 50]
 [ 1 75]]
X=X.reshape(3,2)
Y=np.array([10,7,12])
print(Y.reshape(3,1))
[[10]
 [ 7]
 [12]]
Y=Y.reshape(3,1)

b=((linalg.inv(X.T.dot(X))).dot(X.T)).dot(Y)
print(b)
[[-2.34210526]
 [ 0.19473684]]

"""
"""
Найдите оптимальные коэффициенты для построения линейной регрессии.

На вход вашему решению будет подано название csv-файла, из которого нужно считать данные. 
Пример можно посмотреть здесь. Загрузить их можно следующим образом:

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
Ваша задача — подсчитать вектор коэффициентов линейной регрессии для предсказания 
первой переменной (первого столбца данных) по всем остальным. 
Напомним, что модель линейной регрессии — это y=β0+β1x1+⋯+βnxny=β0+β1x1+⋯+βnxn.

Напечатайте коэффициенты линейной регрессии, начиная с β0β0, через пробел. 
Мы будем проверять совпадения с точностью до 4 знаков после запятой.

Методы и приёмы, которые мы ещё не упоминали и которые могут вам помочь в процессе
 решения (могут являться подсказками!):

np.hstack((array1, array2, ...))  # склеивает по строкам массивы, являющиеся компонентами 
кортежа, поданного на вход; массивы должны совпадать по всем измерениям, кроме второго
np.ones_like(array)  # создаёт массив, состоящий из единиц, идентичный по форме массиву array
"delim".join(array)  # возвращает строку, состоящую из элементов array, 
разделённых символами "delim"
map(str, array)  # применяет функцию str к каждому элементу array

Sample Input:
https://stepic.org/media/attachments/lesson/16462/boston_houses.csv
Sample Output:
-3.65580428507 -0.216395502369 0.0737305981755 4.41245057691 -25.4684487841 7.14320155075 -1.30108767765


import urllib
from urllib import request
import numpy as np
import numpy.linalg as linalg

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
# here goes your solution
Y=np.array(data[:,0]).reshape(data.shape[0],1)
X=np.array(data)
X[:,0]=1
b = ((linalg.inv(X.T.dot(X))).dot(X.T)).dot(Y)
print(' '.join(map(str, b[:,0])))

--------------- alternate

import numpy as np
import urllib
from urllib import request
f = urllib.request.urlopen(input())
X = np.loadtxt(f, delimiter=',', skiprows=1)
y = np.array([i for i in X[:,0]])
X[:,0] = 1
b = (np.linalg.inv(X.T.dot(X))).dot(X.T.dot(y))
for i in b:
    print(i, end=' ')
------------------ alternate
import urllib
from urllib import request
import numpy as np
from scipy import linalg as la
f = urllib.request.urlopen(input())  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
y = np.array(data[:,0])
data[:,0] = 1
bet=la.inv(data.T.dot(data)).dot(data.T).dot(y)
print(*bet)
----------------------alternate
import urllib
from urllib import request
import numpy as np
from numpy import linalg as la

fname = input()
if (fname == '') :
	fname = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'
f = urllib.request.urlopen(fname)
data = np.loadtxt(f, delimiter=',', skiprows=1)

y = data[:,0].reshape(data.shape[0],1)
x = np.hstack((np.ones((data.shape[0],1)), data[:,1:]))

b = la.inv(x.T.dot(x)).dot(x.T).dot(y)
print(*b[:,0])

"""

"""
Задание на доказательство (для продвинутых):

Помимо XOR существует множество других задач, с которыми перцептрон не может справиться. К примеру, он не может отличить два паттерна, если мы разрешаем перенос их через край (дальше - подробнее)

Представьте себе две разных бинарных бегущих строки (два разных паттерна): 

Строка типа AA: 

Строка типа BB: 

Мы можем передвигать эти паттерны, перенося через край. При этом тип паттерна считается прежним: 

Можно представить, что мы просто склеиваем края нашей строки, получая непрерывную ленту (кольцо):


Утверждение заключается в том, что перцептрон не может научиться отличать паттерн (кольцо) AA от паттерна BB. Давайте рассмотрим набросок доказательства (тут можно остановить чтение и попробовать доказать самостоятельно, "с нуля"):

Мы бы хотели, чтобы перцептрон всегда выдавал 11 при предъявлении примера, подчиняющегося паттерну AA и 00 при предъявлении примера паттерна BB 

1. Давайте просуммируем значения сумматорной функции на входе перцептрона при предъявлении всевозможных сдвигов паттерна AA. Каждый вес будет учтён столько раз, сколько у нас активных элементов в паттерне AA. В нашем случае, 4 раза. Кроме того, каждый раз при предъявлении примера будет добавляться смещение (bias). Итого,

∑i=1n4⋅wi+n⋅b
∑i=1n4⋅wi+n⋅b
где wiwi - вес для ii-той позиции.
2. Аналогично для паттерна BB.

Придумайте ключевую идею (3 пункт), которая показывает наличие противоречия в первых двух пунктах, если мы предполагаем, что нам удалось правильно классифицировать все примеры.

Пример правильного решения:
Мы хотим получить такие веса, чтобы для паттерна A в любом его предъявлении сумматорная функция выдавала положительное значение (тогда перцептрон для паттерну A будет всегда выдавать 1). Следовательно, если мы сложим значения сумматорной функции на всех вариантах паттерна A, то получим ∑ni=1awi+nb∑i=1nawi+nb, где aa — количество активных клеток в паттерне (у нас 4). И так как сумматорная функция должна быть всегда положительна, ∑ni=1awi+nb>0∑i=1nawi+nb>0.
Для паттерна B в любом его предъявлении сумматорная функция должна выдавать неположительные значения. Следовательно, сумма значений сумматорной функции на всех вариантах паттерна B тоже должна быть неположительна. В паттерне B тоже aa активных клеток, поэтому сумма значений сумматорной функции равна ∑ni=1awi+nb<0∑i=1nawi+nb<0.
Итак,
{∑ni=1awi+nb≤0.
{∑i=1nawi+nb>0.
Это невозможно ни при каких ww и bb, следовательно, набора весов, позволяющего перцептрону разделить два паттерна с одинаковым количеством активных клеток, не существует.
"""


"""
В этом уроке собраны упражнения по программированию для второй недели.

Сперва вам необходимо скачать задания. У вас есть два варианта:

Скачать удобный Jupyter notebook (далее «ноутбук», кто придумает лучше — пишите в комментарии) с картинками, легко читаемыми пояснениями и дополнительными интерактивными визуализациями, которые будут начинать работать по мере выполнения заданий.
Посмотреть на ноутбук из первого пункта в браузере: картинки, пояснения, одна визуализация, но никакой интерактивности и никаких анимаций.
Проблема с ноутбуком только одна — вы можете не знать, что это и как этим пользоваться. Хорошая новость заключается в том, что «учиться» пользоваться jupyter notebook вам сейчас не нужно. Им нужно просто пользоваться =) 
Ладно, две проблемы: ещё у вас может не быть установлен пакет, которым мы пользовались для построения графиков, matplotlib. Это решается легко: conda install matplotlib, pip3 install matplotlib или что-то аналогичное в зависимости от конфигурации вашей системы.

Jupyter notebook — это браузерное приложение, которое вы запускаете на своём компьютере. Вы получаете возможность у себя в браузере читать/писать текст с разметкой (Markdown) и формулами (MathJax, примерно такие же, как на Степике, только не настолько глючные =) ). Но главное — вы можете писать и выполнять код (с подсветкой синтаксиса и подсказками) на Python (и ещё на более чем 40 языках, по словам сайта проекта). Это действительно удобно и много где используется, очень рекомендуем попробовать. 

Весь наш ноутбук состоит из ячеек двух типов: ячейки с кодом и ячейки с текстом. Выполнить ячейку с кодом можно, выделив её и нажав на кнопку play (или Shift+Enter). Чтобы добавить ячейку, выделите какую-нибудь из имеющихся и нажмите B (добавить снизу) или A (сверху). Чтобы удалить — дважды нажмите D. Сменить тип ячейки: Y — на ячейку с кодом,  M — на ячейку с текстом. Чтобы поменять что-то внутри ячейки — нажмите на неё дважды, чтобы войти в режим редактирования. Чтобы выйти из режима редактирования содержания ячейки — нажмите Esc. Интерфейс очень интуитивный и все то же самое можно делать, кликая мышкой по иконкам.

Как установить: conda install jupyter, pip3 install jupyter или что-то аналогичное в зависимости от конфигурации вашей системы. Как запустить: открываете терминал там, где лежит скачанным наш ноутбук, пишете jupyter notebook, жмёте Enter, в вашем браузере открывается список файлов, нажимаете на наш ноутбук и погружаетесь (если слово «терминал» вас пугает - может сработать двойной клик =) ).

Чтобы получить все интерактивные визуализации, вам надо не забывать запускать все клетки с кодом, в которых содержится их описание. Для тех, кто с этим справится, есть отдельное задание на 8 баллов.

Альтернатива - можно весь код перенести в обычный Python скрипт, с минимальными исправлениями всё должно работать. Бонусы: можно крутить графики, которые в ноутбуке статичны. Минусы: что-то может сломаться.

Итак, ссылки:

статически отрисованная версия ноутбука,
репозиторий на GitHub с ноутбуком, данными и картинками.
Задания сформулированы в ноутбуке. Сдавать ваши функции необходимо в соответствующих степах этого урока.

Как и во всём курсе, в ноутбуке код написан на Python3. Небольшие изменения для Python2 предложил @Akarazeev: описание, diff, patch.

Удачи ;)

https://nbviewer.jupyter.org/github/stacymiller/stepic_neural_networks_public/blob/master/HW_1/Hw_1_student_version.ipynb
https://github.com/stacymiller/stepic_neural_networks_public


Реализуйте метод vectorized_forward_pass класса Perceptron. Когда вы начнёте решать задачу, вам нужно будет просто скопировать соответствующую функцию, которую вы написали в ноутбуке (без учёта отступов; шаблон в поле ввода ответа уже будет, ориентируйтесь по нему). Сигнатура функции указана в ноутбуке, она остаётся неизменной.

n — количество примеров, m — количество входов. Размерность входных данных input_matrix — (n, m), размерность вектора весов — (m, 1), смещение (bias) — отдельно. vectorized_forward_pass должен возвращать массив формы (n, 1), состоящий либо из 0 и 1, либо из True и False.

Обратите внимание, необходимо векторизованное решение, то есть без циклов и операторов ветвления. Используйте свойства умножения матриц и возможность эффективно применять какую-нибудь операцию к каждому элементу np.array, чтобы с минимумом кода получить желаемый результат. Например, 

>>> my_vec = np.array([-1, 2, 3]) 
>>> is_positive = my_vec > 0
>>> is_positive
array([False,  True,  True], dtype=bool)


import numpy as np

def vectorized_forward_pass(self, input_matrix):        
    return input_matrix.dot(self.w)+self.b>0
"""


"""
В данном степе вам нужно реализовать метод train_on_single_example класса Perceptron, который получает на вход один набор входных активаций размерности (m,1) и правильный ответ (число 0 или 1), после чего обновляет веса в соответствии с правилом обучения перцептрона. Когда вы начнёте решать задачу, вам нужно будет просто скопировать соответствующую функцию, которую вы написали в ноутбуке (без учёта отступов; шаблон в поле ввода ответа уже будет, ориентируйтесь по нему). Сигнатура функции указана в ноутбуке, она остаётся неизменной.

Обязательно проверяйте размерности на соответствие указанным в задании и в сигнатуре функции!

Дополнительное ограничение: в данной функции нельзя использовать операторы ветвления и циклы. Мы не сможем это проверить во всех случаях (но, возможно, ваше решение с циклом не сможет уложиться в отведённый решению период работы), так что ответственность за выполнение этого ограничения ложится на вашу совесть.

import numpy as np

def train_on_single_example(self, example, y):
    y_ = (self.w.T.dot(example) + self.b)>0
    self.w += (y - y_)*example
    self.b += (y - y_)
    return (y-y_)

--------- alternate
def train_on_single_example(self, example, y):
    answer = self.forward_pass(example)
    diff = y - answer
    self.b += diff
    self.w += example * diff
    return abs(diff)
"""

"""
Реализуйте методы activation и summatory класса Neuron. Когда вы начнёте решать задачу, вам нужно будет просто скопировать соответствующую функцию, которую вы написали в ноутбуке (без учёта отступов; шаблон в поле ввода ответа уже будет, ориентируйтесь по нему). Сигнатура функции указана в ноутбуке, она остаётся неизменной.

n — количество примеров, m — количество входов. Размерность входных данных input_matrix — (n, m), размерность вектора весов — (m, 1). vectorized_forward_pass должен возвращать массив формы (n, 1), состоящий из чисел (float). Мы будем проверять именно правильность ответа, который возвращает vectorized_forward_pass.
"""
import numpy as np

Jupyter NotebookLogout neural_networks Last Checkpoint: 18 hours ago (autosaved) 
Python 3 
File
Edit
View
Insert
Cell
Kernel
Widgets
Help
CellToolbar
In [1]:

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
import numpy as np
import random
import time
​
from functools import partial
from ipywidgets import interact, RadioButtons, IntSlider, FloatSlider, Dropdown, BoundedFloatText
from numpy.linalg import norm
​
random.seed(42)
In [2]:

%matplotlib inline
data = np.loadtxt("data.csv", delimiter=",")
pears = data[:, 2] == 1
apples = np.logical_not(pears)
plt.scatter(data[apples][:, 0], data[apples][:, 1], color = "red")
plt.scatter(data[pears][:, 0], data[pears][:, 1], color = "green")
plt.xlabel("yellowness")
plt.ylabel("symmetry")
plt.show()
%matplotlib inline
data = np.loadtxt("data.csv", delimiter=",")
pears = data[:, 2] == 1
apples = np.logical_not(pears)
plt.scatter(data[apples][:, 0], data[apples][:, 1], color = "red")
plt.scatter(data[pears][:, 0], data[pears][:, 1], color = "green")
plt.xlabel("yellowness")
plt.ylabel("symmetry")
plt.show()

In [3]:

my_vec = np.array([-1, 2, 3]) 
is_positive = my_vec > 0
is_positive
Out[3]:
array([False,  True,  True], dtype=bool)
In [4]:

class Perceptron:
​
    def __init__(self, w, b):
        """
        Инициализируем наш объект - перцептрон.
        w - вектор весов размера (m, 1), где m - количество переменных
        b - число
        """
        
        self.w = w
        self.b = b
​
    def forward_pass(self, single_input):
        """
        Метод рассчитывает ответ перцептрона при предъявлении одного примера
        single_input - вектор примера размера (m, 1).
        Метод возвращает число (0 или 1) или boolean (True/False)
        """
        
        result = 0
        for i in range(0, len(self.w)):
            result += self.w[i] * single_input[i]
        result += self.b
        
        if result > 0:
            return 1
        else:
            return 0
        
    def vectorized_forward_pass(self, input_matrix):        
        return input_matrix.dot(self.w)+self.b>0
    
    def train_on_single_example(self, example, y):
        y_ = (self.w.T.dot(example) + self.b)>0
        self.w += (y - y_)*example
        self.b += (y - y_)
        return (y-y_)
    
    def train_until_convergence(self, input_matrix, y, max_steps=1e8):
        """
        input_matrix - матрица входов размера (n, m),
        y - вектор правильных ответов размера (n, 1) (y[i] - правильный ответ на пример input_matrix[i]),
        max_steps - максимальное количество шагов.
        Применяем train_on_single_example, пока не перестанем ошибаться или до умопомрачения.
        Константа max_steps - наше понимание того, что считать умопомрачением.
        """
        i = 0
        errors = 1
        while errors and i < max_steps:
            i += 1
            errors = 0
            for example, answer in zip(input_matrix, y):
                example = example.reshape((example.size, 1))
                error = self.train_on_single_example(example, answer)
                errors += int(error)  # int(True) = 1, int(False) = 0, так что можно не делать if
​
In [5]:

def plot_line(coefs):
    """
    рисует разделяющую прямую, соответствующую весам, переданным в coefs = (weights, bias), 
    где weights - ndarray формы (2, 1), bias - число
    """
    w, bias = coefs
    a, b = - w[0][0] / w[1][0], - bias / w[1][0]
    xx = np.linspace(*plt.xlim())
    line.set_data(xx, a*xx + b)
In [6]:

def step_by_step_weights(p, input_matrix, y, max_steps=1e6):
    """
    обучает перцептрон последовательно на каждой строчке входных данных, 
    возвращает обновлённые веса при каждом их изменении
    p - объект класса Perceptron
    """
    i = 0
    errors = 1
    while errors and i < max_steps:
        i += 1
        errors = 0
        for example, answer in zip(input_matrix, y):
            example = example.reshape((example.size, 1))
            
            error = p.train_on_single_example(example, answer)
            errors += error  # здесь мы упадём, если вы забыли вернуть размер ошибки из train_on_single_example
            if error:  # будем обновлять положение линии только тогда, когда она изменила своё положение
                yield p.w, p.b
                
    for _ in range(20): yield p.w, p.b
In [7]:

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as p3
import numpy as np
import random
import time
​
from functools import partial
from ipywidgets import interact, RadioButtons, IntSlider, FloatSlider, Dropdown, BoundedFloatText
from numpy.linalg import norm
​
random.seed(42) # начальное состояние генератора случайных чисел, чтобы можно было воспроизводить результаты.
​
%matplotlib inline
data = np.loadtxt("data.csv", delimiter=",")
pears = data[:, 2] == 1
apples = np.logical_not(pears)
plt.scatter(data[apples][:, 0], data[apples][:, 1], color = "red")
plt.scatter(data[pears][:, 0], data[pears][:, 1], color = "green")
plt.xlabel("yellowness")
plt.ylabel("symmetry")
plt.show()

In [8]:

def create_perceptron(m):
    """Создаём перцептрон со случайными весами и m входами"""
    w = np.random.random((m, 1))
    return Perceptron(w, 1)
In [9]:

def test_v_f_p(n, m):
    """
    Расчитывает для перцептрона с m входами
    с помощью методов forward_pass и vectorized_forward_pass
    n ответов перцептрона на случайных данных.
    Возвращает время, затраченное vectorized_forward_pass и forward_pass
    на эти расчёты.
    """
    
    p = create_perceptron(m)
    input_m = np.random.random_sample((n, m))
    
    start = time.clock()
    vec = p.vectorized_forward_pass(input_m)
    end = time.clock()
    vector_time = end - start
    
    start = time.clock()
    for i in range(0, n):
        p.forward_pass(input_m[i]) 
    end = time.clock()
    plain_time = end - start
​
    return [vector_time, plain_time]
In [10]:

def mean_execution_time(n, m, trials=100):
    """среднее время выполнения forward_pass и vectorized_forward_pass за trials испытаний"""
    
    return np.array([test_v_f_p(m, n) for _ in range(trials)]).mean(axis=0)
​
def plot_mean_execution_time(n, m):
    """рисует графики среднего времени выполнения forward_pass и vectorized_forward_pass"""
    
    mean_vectorized, mean_plain = mean_execution_time(int(n), int(m))
    p1 = plt.bar([0], mean_vectorized,  color='g')
    p2 = plt.bar([1], mean_plain, color='r')
​
    plt.ylabel("Time spent")
    plt.yticks(np.arange(0, mean_plain))
​
    plt.xticks(range(0,1))
    plt.legend(("vectorized","non - vectorized"))
​
    plt.show()
​
interact(plot_mean_execution_time, 
            n=RadioButtons(options=["1", "10", "100"]),
            m=RadioButtons(options=["1", "10", "100"], separator=" "));

In [11]:

%matplotlib nbagg
​
np.random.seed(1)
fig = plt.figure()
plt.scatter(data[apples][:, 0], data[apples][:, 1], color = "red", marker=".", label="Apples")
plt.scatter(data[pears][:, 0], data[pears][:, 1], color = "green", marker=".", label="Pears")
plt.xlabel("yellowness")
plt.ylabel("symmetry")
line, = plt.plot([], [], color="black", linewidth=2)  # создаём линию, которая будет показывать границу разделения
​
from matplotlib.animation import FuncAnimation
​
perceptron_for_weights_line = create_perceptron(2)  # создаём перцептрон нужной размерности со случайными весами
​
from functools import partial
weights_ani = partial(
    step_by_step_weights, p=perceptron_for_weights_line, input_matrix=data[:, :-1], y=data[:, -1][:,np.newaxis]
)  # про partial почитайте на https://docs.python.org/3/library/functools.html#functools.partial
​
ani = FuncAnimation(fig, func=plot_line, frames=weights_ani, blit=False, interval=10, repeat=True)
# если Jupyter не показывает вам анимацию - раскомментируйте строчку ниже и посмотрите видео
#ani.save("perceptron_seeking_for_solution.mp4", fps=15)
plt.show()
​
## Не забудьте остановить генерацию новых картинок, прежде чем идти дальше (кнопка "выключить" в правом верхнем углу графика)


In [12]:

def step_by_step_errors(p, input_matrix, y, max_steps=1e6):
    """
    обучает перцептрон последовательно на каждой строчке входных данных, 
    на каждом шаге обучения запоминает количество неправильно классифицированных примеров
    и возвращает список из этих количеств
    """
    def count_errors():
        return np.abs(p.vectorized_forward_pass(input_matrix).astype(np.int) - y).sum()
    errors_list = [count_errors()]
    i = 0
    errors = 1
    while errors and i < max_steps:
        i += 1
        errors = 0
        for example, answer in zip(input_matrix, y):
            example = example.reshape((example.size, 1))
            
            error = p.train_on_single_example(example, answer)
            errors += error
            errors_list.append(count_errors())
    return errors_list
In [13]:

%matplotlib inline
perceptron_for_misclassification = create_perceptron(2)
errors_list = step_by_step_errors(perceptron_for_misclassification, input_matrix=data[:, :-1], y=data[:, -1][:,np.newaxis])
plt.plot(errors_list);
plt.ylabel("Number of errors")
plt.xlabel("Algorithm step number");

In [14]:

def get_vector(p):
    """возвращает вектор из всех весов перцептрона, включая смещение"""
    v = np.array(list(p.w.ravel()) + [p.b])
    return v
In [15]:

def step_by_step_distances(p, ideal, input_matrix, y, max_steps=1e6):
    """обучает перцептрон p и записывает каждое изменение расстояния от текущих весов до ideal"""
    distances = [norm(get_vector(p) - ideal)]
    i = 0
    errors = 1
    while errors and i < max_steps:
        i += 1
        errors = 0
        for example, answer in zip(input_matrix, y):
            example = example.reshape((example.size, 1))
            
            error = p.train_on_single_example(example, answer)
            errors += error
            if error:
                distances.append(norm(get_vector(p) - ideal))
    return distances
In [16]:

%matplotlib inline
​
np.random.seed(42)
init_weights = np.random.random_sample(3)
w, b = init_weights[:-1].reshape((2, 1)), init_weights[-1]
ideal_p = Perceptron(w.copy(), b.copy())
ideal_p.train_until_convergence(data[:, :-1], data[:, -1][:,np.newaxis])
ideal_weights = get_vector(ideal_p)
​
new_p = Perceptron(w.copy(), b.copy())
distances = step_by_step_distances(new_p, ideal_weights, data[:, :-1], data[:, -1][:,np.newaxis])
​
plt.xlabel("Number of weight updates")
plt.ylabel("Distance between good and current weights")
plt.plot(distances);

In [17]:

## Определим разные полезные функции
​
def sigmoid(x):
    """сигмоидальная функция, работает и с числами, и с векторами (поэлементно)"""
    return 1 / (1 + np.exp(-x))
​
def sigmoid_prime(x):
    """производная сигмоидальной функции, работает и с числами, и с векторами (поэлементно)"""
    return sigmoid(x) * (1 - sigmoid(x))
In [18]:

class Neuron:
    
    def __init__(self, weights, activation_function=sigmoid, activation_function_derivative=sigmoid_prime):
        """
        weights - вертикальный вектор весов нейрона формы (m, 1), weights[0][0] - смещение
        activation_function - активационная функция нейрона, сигмоидальная функция по умолчанию
        activation_function_derivative - производная активационной функции нейрона
        """
        
        assert weights.shape[1] == 1, "Incorrect weight shape"
        
        self.w = weights
        self.activation_function = activation_function
        self.activation_function_derivative = activation_function_derivative
        
    def forward_pass(self, single_input):
        """
        активационная функция логистического нейрона
        single_input - вектор входов формы (m, 1), 
        первый элемент вектора single_input - единица (если вы хотите учитывать смещение)
        """
        
        result = 0
        for i in range(self.w.size):
            result += float(self.w[i] * single_input[i])
        return self.activation_function(result)
    
    def summatory(self, input_matrix):
        """
        Вычисляет результат сумматорной функции для каждого примера из input_matrix. 
        input_matrix - матрица примеров размера (n, m), каждая строка - отдельный пример,
        n - количество примеров, m - количество переменных.
        Возвращает вектор значений сумматорной функции размера (n, 1).
        """
        # Этот метод необходимо реализовать
        return input_matrix.dot(self.w)
​
    def activation(self, summatory_activation):
        """
        Вычисляет для каждого примера результат активационной функции,
        получив на вход вектор значений сумматорной функций
        summatory_activation - вектор размера (n, 1), 
        где summatory_activation[i] - значение суммматорной функции для i-го примера.
        Возвращает вектор размера (n, 1), содержащий в i-й строке 
        значение активационной функции для i-го примера.
        """
        # Этот метод необходимо реализовать
        
        return self.activation_function(summatory_activation)
    
    def vectorized_forward_pass(self, input_matrix):
        """
        Векторизованная активационная функция логистического нейрона.
        input_matrix - матрица примеров размера (n, m), каждая строка - отдельный пример,
        n - количество примеров, m - количество переменных.
        Возвращает вертикальный вектор размера (n, 1) с выходными активациями нейрона
        (элементы вектора - float)
        """
        return self.activation(self.summatory(input_matrix))
        
    def SGD(self, X, y, batch_size, learning_rate=0.1, eps=1e-6, max_steps=200):
        """
        Внешний цикл алгоритма градиентного спуска.
        X - матрица входных активаций (n, m)
        y - вектор правильных ответов (n, 1)
        
        learning_rate - константа скорости обучения
        batch_size - размер батча, на основании которого 
        рассчитывается градиент и совершается один шаг алгоритма
        
        eps - критерий остановки номер один: если разница между значением целевой функции 
        до и после обновления весов меньше eps - алгоритм останавливается. 
        Вторым вариантом была бы проверка размера градиента, а не изменение функции,
        что будет работать лучше - неочевидно. В заданиях используйте первый подход.
        
        max_steps - критерий остановки номер два: если количество обновлений весов 
        достигло max_steps, то алгоритм останавливается
        
        Метод возвращает 1, если отработал первый критерий остановки (спуск сошёлся) 
        и 0, если второй (спуск не достиг минимума за отведённое время).
        """
        
        # Этот метод необходимо реализовать
        step=0
        n = X.shape[0]
        res = 0 
        a=np.arange(n)
        while(step<max_steps)&(res==0):
            np.random.shuffle(a)
            rnd = np.random.choice(a,batch_size, replace=False)
            newX = X[rnd]
            newY = y[rnd]
            res = self.update_mini_batch(newX,newY,learning_rate,eps)
            step +=1
        return res
    
    def update_mini_batch(self, X, y, learning_rate, eps):
        """
        X - матрица размера (batch_size, m)
        y - вектор правильных ответов размера (batch_size, 1)
        learning_rate - константа скорости обучения
        eps - критерий остановки номер один: если разница между значением целевой функции 
        до и после обновления весов меньше eps - алгоритм останавливается. 
        
        Рассчитывает градиент (не забывайте использовать подготовленные заранее внешние функции) 
        и обновляет веса нейрона. Если ошибка изменилась меньше, чем на eps - возвращаем 1, 
        иначе возвращаем 0.
        """
        # Этот метод необходимо реализовать
        
        # loss before update
        #loss0 = 0.5 * np.mean((self.vectorized_forward_pass(X) - y) ** 2)        
        # update weights
        #Xout = self.summatory(X)
        #activ = self.activation_function(Xout)
        #deriv = self.activation_function_derivative(Xout)       
        #grad = np.dot(np.transpose((activ - y) * deriv), X) / (X.shape[0])
        #self.w = self.w - learning_rate * grad.T
        # loss after update
        #loss1 = 0.5 * np.mean((self.vectorized_forward_pass(X) - y) ** 2)
        #return 1 if abs(loss1 - loss0) < eps else 0
    
        ##### alternative my
        grad = compute_grad_analytically(self, X, y)
        y0 = J_quadratic(self, X, y) #0.5 * np.mean((self.vectorized_forward_pass(X) - y) ** 2)
        self.w -= learning_rate * grad
        y1 = J_quadratic(self, X, y) #0.5 * np.mean((self.vectorized_forward_pass(X) - y) ** 2)
        delta = y1 - y0
        return 1 if abs(delta) < eps else 0
    
    #--------- alternate
    #def SGD(self, X, y, batch_size, learning_rate=0.1, eps=1e-6, max_steps=200):
    #    for i in range(max_steps):
    #        sample_ids = np.random.choice(range(X.shape[0]), batch_size, replace=False)
    #        Xsample = X[sample_ids, :]
    #        ysample = y[sample_ids]
    #        if self.update_mini_batch(Xsample, ysample, learning_rate, eps):
    #            return 1
    #    return 0
​
    #def update_mini_batch(self, X, y, learning_rate, eps):
    #    loss0 = J_quadratic(self, X, y)
    #    grad = compute_grad_analytically(self, X, y)
    #    self.w = self.w - learning_rate * grad
    #    loss1 = J_quadratic(self, X, y)
    #    return 1 if abs(loss1 - loss0) < eps else 0
    
def J_quadratic(neuron, X, y):
    """
    Оценивает значение квадратичной целевой функции.
    Всё как в лекции, никаких хитростей.
​
    neuron - нейрон, у которого есть метод vectorized_forward_pass, предсказывающий значения на выборке X
    X - матрица входных активаций (n, m)
    y - вектор правильных ответов (n, 1)
​
    Возвращает значение J (число)
    """
​
    assert y.shape[1] == 1, 'Incorrect y shape'
​
    return 0.5 * np.mean((neuron.vectorized_forward_pass(X) - y) ** 2)
​
def J_quadratic_derivative(y, y_hat):
    """
    Вычисляет вектор частных производных целевой функции по каждому из предсказаний.
    y_hat - вертикальный вектор предсказаний,
    y - вертикальный вектор правильных ответов,
​
    В данном случае функция смехотворно простая, но если мы захотим поэкспериментировать 
    с целевыми функциями - полезно вынести эти вычисления в отдельный этап.
​
    Возвращает вектор значений производной целевой функции для каждого примера отдельно.
    """
​
    assert y_hat.shape == y.shape and y_hat.shape[1] == 1, 'Incorrect shapes'
​
    return (y_hat - y) / len(y)
​
def compute_grad_analytically(neuron, X, y, J_prime=J_quadratic_derivative):
        """
        Аналитическая производная целевой функции
        neuron - объект класса Neuron
        X - вертикальная матрица входов формы (n, m), на которой считается сумма квадратов отклонений
        y - правильные ответы для примеров из матрицы X
        J_prime - функция, считающая производные целевой функции по ответам
​
        Возвращает вектор размера (m, 1)
        """
​
        # Вычисляем активации
        # z - вектор результатов сумматорной функции нейрона на разных примерах
​
        z = neuron.summatory(X)
        y_hat = neuron.activation(z)
​
        # Вычисляем нужные нам частные производные
        dy_dyhat = J_prime(y, y_hat)
        dyhat_dz = neuron.activation_function_derivative(z)
​
        # осознайте эту строчку:
        dz_dw = X
​
        # а главное, эту:
        grad = ((dy_dyhat * dyhat_dz).T).dot(dz_dw)
​
        # можно было написать в два этапа. Осознайте, почему получается одно и то же
        # grad_matrix = dy_dyhat * dyhat_dz * dz_dw
        # grad = np.sum(, axis=0)
​
        # Сделаем из горизонтального вектора вертикальный
        grad = grad.T
​
        return grad
    
def compute_grad_numerically(neuron, X, y, J=J_quadratic, eps=10e-2):
        """
        Численная производная целевой функции
        neuron - объект класса Neuron
        X - вертикальная матрица входов формы (n, m), на которой считается сумма квадратов отклонений
        y - правильные ответы для тестовой выборки X
        J - целевая функция, градиент которой мы хотим получить
        eps - размер $\delta w$ (малого изменения весов)
        """
​
        initial_cost = J(neuron, X, y)
        w_0 = neuron.w
        num_grad = np.zeros(w_0.shape)
​
        for i in range(len(w_0)):
​
            old_wi = neuron.w[i].copy()
            # Меняем вес
            neuron.w[i] += eps
​
            # Считаем новое значение целевой функции и вычисляем приближенное значение градиента
            num_grad[i] = (J(neuron, X, y) - initial_cost)/eps
​
            # Возвращаем вес обратно. Лучше так, чем -= eps, чтобы не накапливать ошибки округления
            neuron.w[i] = old_wi
​
        # проверим, что не испортили нейрону веса своими манипуляциями
        assert np.allclose(neuron.w, w_0), "МЫ ИСПОРТИЛИ НЕЙРОНУ ВЕСА"
        return num_grad
In [19]:

np.random.seed(42)
n = 10
m = 5
​
X = 20 * np.random.sample((n, m)) - 10
y = (np.random.random(n) < 0.5).astype(np.int)[:, np.newaxis]
w = 2 * np.random.random((m, 1)) - 1
​
neuron = Neuron(w)
neuron.update_mini_batch(X, y, 0.1, 1e-5)
#neuron.SGD(X, y, 2, 0.1, 1e-5)
Out[19]:
0
In [20]:

print(neuron.w)
[[-0.22368982]
 [-0.45599204]
 [ 0.65727411]
 [-0.28380677]
 [-0.43011026]]
In [35]:

# Подготовим данные
​
X = data[:, :-1]
y = data[:, -1]
​
X = np.hstack((np.ones((len(y), 1)), X))
y = y.reshape((len(y), 1)) # Обратите внимание на эту очень противную и важную строчку
​
​
# Создадим нейрон
​
w = np.random.random((X.shape[1], 1))
neuron = Neuron(w, activation_function=sigmoid, activation_function_derivative=sigmoid_prime)
​
# Посчитаем пример
num_grad = compute_grad_numerically(neuron, X, y, J=J_quadratic)
an_grad = compute_grad_analytically(neuron, X, y, J_prime=J_quadratic_derivative)
​
print("Численный градиент: \n", num_grad)
print("Аналитический градиент: \n", an_grad)
Численный градиент: 
 [[ 0.02517702]
 [ 0.00028275]
 [ 0.0283814 ]]
Аналитический градиент: 
 [[ 0.02361927]
 [-0.00074347]
 [ 0.02855421]]
In [36]:

def print_grad_diff(eps):
    num_grad = compute_grad_numerically(neuron, X, y, J=J_quadratic, eps=float(eps))
    an_grad = compute_grad_analytically(neuron, X, y, J_prime=J_quadratic_derivative)
    print(np.linalg.norm(num_grad-an_grad))
    
interact(print_grad_diff, 
            eps=RadioButtons(options=["3", "1", "0.1", "0.001", "0.0001"]), separator=" ");
0.0146060061038
In [37]:

def compute_grad_numerically_2(neuron, X, y, J=J_quadratic, eps=10e-2):
    """
    Численная производная целевой функции.
    neuron - объект класса Neuron с вертикальным вектором весов w,
    X - вертикальная матрица входов формы (n, m), на которой считается сумма квадратов отклонений,
    y - правильные ответы для тестовой выборки X,
    J - целевая функция, градиент которой мы хотим получить,
    eps - размер $\delta w$ (малого изменения весов).
    """
    
    # эту функцию необходимо реализовать
    initial_cost = J(neuron, X, y)
    w_0 = neuron.w
    num_grad = np.zeros(w_0.shape)
​
    for i in range(len(w_0)):
​
        old_wi = neuron.w[i].copy()
        # Меняем вес на +
        neuron.w[i] += eps
        J_plus_delta = J(neuron, X, y)
        # Меняем вес на -
        neuron.w[i] -= eps
        neuron.w[i] -= eps
        J_minus_delta = J(neuron, X, y)
        # Считаем новое значение целевой функции и вычисляем приближенное значение градиента
        num_grad[i] = (J_plus_delta - J_minus_delta)/(2*eps)
​
        # Возвращаем вес обратно. Лучше так, чем -= eps, чтобы не накапливать ошибки округления
        neuron.w[i] = old_wi
​
    # проверим, что не испортили нейрону веса своими манипуляциями
    assert np.allclose(neuron.w, w_0), "МЫ ИСПОРТИЛИ НЕЙРОНУ ВЕСА"
    return num_grad
    
    #------------ alternate
    #w_0 = neuron.w
    #num_grad = np.zeros(w_0.shape)    
    #for i in range(len(w_0)):        
    #    old_wi = neuron.w[i].copy()
    #    
    #    neuron.w[i] = old_wi + eps
    #    plus_cost = J(neuron, X, y)
    #    
    #    neuron.w[i] = old_wi - eps
    #    minus_cost = J(neuron, X, y)        
    #    
    #    num_grad[i] = (plus_cost - minus_cost)/(2*eps)
    #    neuron.w[i] = old_wi                
    #return num_grad
In [ ]:

​
In [38]:

def print_grad_diff_2(eps):
    num_grad = compute_grad_numerically_2(neuron, X, y, J=J_quadratic, eps=float(eps))
    an_grad = compute_grad_analytically(neuron, X, y, J_prime=J_quadratic_derivative)
    print(np.linalg.norm(num_grad-an_grad))
    
interact(print_grad_diff_2, 
            eps=RadioButtons(options=["3", "1", "0.1", "0.001", "0.0001"]), separator=" ");
0.0334794558243
In [39]:

def J_by_weights(weights, X, y, bias):
    """
    Посчитать значение целевой функции для нейрона с заданными весами.
    Только для визуализации
    """
    new_w = np.hstack((bias, weights)).reshape((3,1))
    return J_quadratic(Neuron(new_w), X, y)
In [26]:

#%matplotlib qt4
%matplotlib inline
​
max_b = 40
min_b = -40
max_w1 = 40
min_w1 = -40
max_w2 = 40
min_w2 = -40
​
g_bias = 0 # график номер 2 будет при первой генерации по умолчанию иметь то значение b, которое выставлено в первом
X_corrupted = X.copy()
y_corrupted = y.copy()
​
@interact(fixed_bias=FloatSlider(min=min_b, max=max_b, continuous_update=False), 
          mixing=FloatSlider(min=0, max=1, continuous_update=False, value=0),
          shifting=FloatSlider(min=0, max=1, continuous_update=False, value=0)
            )
def visualize_cost_function(fixed_bias, mixing, shifting):
    """
    Визуализируем поверхность целевой функции на (опционально) подпорченных данных и сами данные.
    Портим данные мы следующим образом: сдвигаем категории навстречу друг другу, на величину, равную shifting 
    Кроме того, меняем классы некоторых случайно выбранных примеров на противоположнее.
    Доля таких примеров задаётся переменной mixing
    
    Нам нужно зафиксировать bias на определённом значении, чтобы мы могли что-нибудь визуализировать.
    Можно посмотреть, как bias влияет на форму целевой функции
    """
    xlim = (min_w1, max_w1)
    ylim = (min_w2, max_w2)
    xx = np.linspace(*xlim, num=101)
    yy = np.linspace(*ylim, num=101)
    xx, yy = np.meshgrid(xx, yy)
    points = np.stack([xx, yy], axis=2)
    
    # не будем портить исходные данные, будем портить их копию
    corrupted = data.copy()
    
    # инвертируем ответы для случайно выбранного поднабора данных
    mixed_subset = np.random.choice(range(len(corrupted)), int(mixing * len(corrupted)), replace=False)
    corrupted[mixed_subset, -1] = np.logical_not(corrupted[mixed_subset, -1])
    
    # сдвинем все груши (внизу справа) на shifting наверх и влево
    pears = corrupted[:, 2] == 1
    apples = np.logical_not(pears)
    corrupted[pears, 0] -= shifting
    corrupted[pears, 1] += shifting
    
    # вытащим наружу испорченные данные
    global X_corrupted, y_corrupted
    X_corrupted = np.hstack((np.ones((len(corrupted),1)), corrupted[:, :-1]))
    y_corrupted = corrupted[:, -1].reshape((len(corrupted), 1))
    
    # посчитаем значения целевой функции на наших новых данных
    calculate_weights = partial(J_by_weights, X=X_corrupted, y=y_corrupted, bias=fixed_bias)
    J_values = np.apply_along_axis(calculate_weights, -1, points)
    
    fig = plt.figure(figsize=(16,5))
    # сначала 3D-график целевой функции
    ax_1 = fig.add_subplot(1, 2, 1, projection='3d')
    surf = ax_1.plot_surface(xx, yy, J_values, alpha=0.3)
    ax_1.set_xlabel("$w_1$")
    ax_1.set_ylabel("$w_2$")
    ax_1.set_zlabel("$J(w_1, w_2)$")
    ax_1.set_title("$J(w_1, w_2)$ for fixed bias = ${}$".format(fixed_bias))
    # потом плоский поточечный график повреждённых данных
    ax_2 = fig.add_subplot(1, 2, 2)
    plt.scatter(corrupted[apples][:, 0], corrupted[apples][:, 1], color = "red", alpha=0.7)
    plt.scatter(corrupted[pears][:, 0], corrupted[pears][:, 1], color = "green", alpha=0.7)
    ax_2.set_xlabel("yellowness")
    ax_2.set_ylabel("symmetry")
    ax_1.scatter(10, -10, 0.1)
​
    plt.show()

In [44]:

@interact(b=BoundedFloatText(value=str(g_bias), min=min_b, max=max_b, description="Enter $b$:"),
          w1=BoundedFloatText(value="0", min=min_w1, max=max_w1, description="Enter $w_1$:"),
          w2=BoundedFloatText(value="0", min=min_w2, max=max_w2, description="Enter $w_2$:"),
          learning_rate=Dropdown(options=["0.01", "0.05", "0.1", "0.5", "1", "5", "10"], 
                                value="0.01", description="Learning rate: ")
         )
def learning_curve_for_starting_point(b, w1, w2, learning_rate=0.01):
    w = np.array([b, w1, w2]).reshape(X_corrupted.shape[1], 1)
    #learning_rate=float(learning_rate)
    learning_rate=30
    neuron = Neuron(w, activation_function=sigmoid, activation_function_derivative=sigmoid_prime)
​
    story = [J_quadratic(neuron, X_corrupted, y_corrupted)]
    for _ in range(2000):
        neuron.SGD(X_corrupted, y_corrupted, 2, learning_rate=learning_rate, max_steps=2)
        story.append(J_quadratic(neuron, X_corrupted, y_corrupted))
    plt.plot(story)
    
    plt.title("Learning curve.\n Final $b={0:.3f}$, $w_1={1:.3f}, w_2={2:.3f}$".format(*neuron.w.ravel()))
    plt.ylabel("$J(w_1, w_2)$")
    plt.xlabel("Weight and bias update number")
    plt.show()

In [ ]:

    
"""
Итак, мы знаем, как посчитать «назад» ошибку из l+1l+1 слоя в ll-й. Чтобы это знание не утекло куда подальше, давайте сразу его запрограммируем. Заодно вспомним различия между .dot и *.

Напишите функцию, которая, используя набор ошибок δl+1δl+1 для nn примеров, матрицу весов Wl+1Wl+1 и набор значений сумматорной функции на ll-м шаге для этих примеров, возвращает значение ошибки δlδl на ll-м слое сети.

Сигнатура: get_error(deltas, sums, weights), где deltas — ndarray формы (nn, nl+1nl+1), содержащий в ii-й строке значения ошибок для ii-го примера из входных данных, sums — ndarray формы (nn, nlnl), содержащий в ii-й строке значения сумматорных функций нейронов ll-го слоя для ii-го примера из входных данных, weights — ndarray формы (nl+1nl+1, nlnl), содержащий веса для перехода между ll-м и l+1l+1-м слоем сети. Требуется вернуть вектор δlδl — ndarray формы (nlnl, 1); мы не проверяем размер (форму) ответа, но это может помочь вам сориентироваться. Все нейроны в сети — сигмоидальные. Функции sigmoid и sigmoid_prime уже определены.

Обратите внимание, в предыдущей задаче мы работали только с одним примером, а сейчас вам на вход подаётся несколько. Не забудьте учесть этот факт и просуммировать всё, что нужно. И разделить тоже. Подсказка: J=1n∑ni=112∣∣y^(i)−y(i)∣∣2⟹∂J∂θ=1n∑ni=1∂∂θ(12∣∣y^(i)−y(i)∣∣2)J=1n∑i=1n12|y^(i)−y(i)|2⟹∂J∂θ=1n∑i=1n∂∂θ(12|y^(i)−y(i)|2) для любого параметра θθ, который не число примеров.
"""
	
import numpy as np
def get_error(deltas, sums, weights):
    """
    compute error on the previous layer of network
    deltas - ndarray of shape (n, n_{l+1})
    sums - ndarray of shape (n, n_l)
    weights - ndarray of shape (n_{l+1}, n_l)
    """
    # here goes your code
    n=deltas.shape[0]
    return sum((deltas.dot(weights))*sigmoid_prime(sums))/n
	
"""
seaborn
heatmap

import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set()
uniform_data = np.random.rand(10,12)
ax = sns.heatmap(uniform_data)


ax = sns.heatmap(uniform_data, vmin=0, vmax=1)


Застревание в локальном минимуме => Попробовать несколько начальных точек (начальных весов) сети

Веса и целевая функция почти/вообще не меняются => Нормировать входы

Переобучение =>Устроить кросс-валидацию

Форма изменения целевой функции хорошая, но обучение протекает долго=>Увеличить learning rate

δL=∇aLJ⊙(aL)′(zL)δL=∇aLJ⊙(aL)′(zL)
δl=((Wl+1)Tδl+1)⊙(al)′(zl)δl=((Wl+1)Tδl+1)⊙(al)′(zl)
∂J∂blj=δlj
"""

"""
http://neuralnetworksanddeeplearning.com/chap2.html
http://statweb.stanford.edu/~tibs/ElemStatLearn/
http://localhost:8888/notebooks/Hw_2_student_version.ipynb
"""