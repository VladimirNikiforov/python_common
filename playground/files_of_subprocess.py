# Файлы в родительском и дочернем процессе

# $cat data.txt
# example string1
# example string2


import os

f = open("data.txt")
foo = f.readline()

if os.fork() == 0:
    foo = f.readline()
    print("child:", foo)
else:
    foo = f.readline()
    print("parent:", foo)
