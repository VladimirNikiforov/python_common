# year = int(input())
# is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
# print(is_leap)

import calendar

# year = int(input())
year = 2017
print(id(year))
print(calendar.isleap(year))
year += 1000
print(id(year))

quote = """Ghjdtyhfdsjhkjlkj@jhgjlkn"""
print(quote.count("h"))

print("hello".capitalize())
print("sdf23".isdigit())
print("3.14" in "Number PI = 3.14159265")

for r in "hello":
    print("Symbol", r)

print(str(345.01))
print(bool("dfg"))

template = "%s - masdsdfgdg. (%s)"
print(template % ("Leaseness", "Heeeekkk"))

# number == %d

print("{} не лгут, но {} пользуются формулами. ({})".format(
    "Цифры", "лжецы", "Robert A.Heinlein"
))

print("{num} Кб должно хватить для любых задач. ({author})".format(
    num=640, author="Bill Gates"
))

subject = "оптимизация"
author = "Donald Knuth"
print(f"Преждевременная {subject} - корень всех зол. ({author})")

num = 8
print(f"Binary: {num:#b}")
num = 2 / 3
print(num)
print(f"{num:.3f}")

# name = input("Input your name: ")
# print(f"Hello, {name}!")

example_bytes = b"hello"
print(type(example_bytes))
print(example_bytes)
for el in example_bytes:
    print(el)

example_string = "привет"
print(type(example_string))
print(example_string)

encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))
for el in encoded_string:
    print(el)

decoded_string = encoded_string.decode()
print(decoded_string)

answer = None
print(type(None))

print(bool(answer))

if not answer:
    print("Ответ не получен!")

income = 0
if not income:
    print("Nothing saved!")

income = None
if income is None:
    print("Haven't started!")
elif not income:
    print("Nothing saved!")
