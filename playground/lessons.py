def week_1():
    def multiply(a, b):
        return a * b


"""

from mypackage.utils import multiply as mlt

if __name__ == "__main__":
    print(mlt(2, 3))
"""


def week_2():
    def lists():

        empty_list = []
        empty_list = list()

        none_list = [None] * 10

        l_collections = ['list', 'tuple', 'dict', 'set']

        print('list' in l_collections)  # searching element in list need linear time!

        user_data = [
            ['Elena', 4.4],
            ['Andrey', 4.2]
        ]

        len(l_collections)  # constant time!

        print(l_collections)
        print(l_collections[0])
        print(l_collections[-1])

        l_collections[3] = 'frozenset'
        print(l_collections)

        range_list = list(range(10))
        print(range_list)

        print(range_list[1:3])
        print(range_list[3:])
        print(range_list[:5])
        print(range_list[::2])
        print(range_list[::-1])
        print(range_list[5:1:-1])
        print(range_list[:] is range_list)

        l_collections = ['list', 'tuple', 'dict', 'set']
        for collection in l_collections:
            print('Learning {}...'.format(collection))

        for idx, collection in enumerate(l_collections):
            print('#{} {}'.format(idx, collection))

        l_collections.append('OrderedDict')
        print(l_collections)

        l_collections.extend(['ponyset', 'unicorndict'])
        print(l_collections)

        l_collections += [None]
        print(l_collections)

        del l_collections[4]
        print(l_collections)

        numbers = [4, 17, 19, 9, 2, 6, 10, 13]
        print(min(numbers))
        print(max(numbers))
        print(sum(numbers))

        tag_list = ['python', 'course', 'coursera']
        print(', '.join(tag_list))

    ####################################
    def sorting():
        import random

        numbers = []
        for _ in range(10):
            numbers.append(random.randint(1, 20))

        print(numbers)

        print(sorted(numbers))
        print(numbers)
        numbers.sort()
        print(numbers)
        print(sorted(numbers, reverse=True))
        numbers.sort(reverse=True)
        print(numbers)
        print(reversed(numbers))
        print(list(reversed(numbers)))

        """ METHODS
        append
        clear
        copy
        count
        extend
        index
        insert
        pop
        remove
        reverse
        sort
        """

    def tuples():
        # Tuples - immutable!
        # неизменяемые, могут содержать эл-ты разных типов, поиск за линейное время
        empty_tuple = ()
        empty_tuple = tuple()

        immutables = (int, str, tuple)

        # but objects inside the tuples could be mutable!
        blink = ([], [])
        blink[0].append(0)
        print(blink)

        print(hash(tuple()))

        one_element_tuple = (1,)
        guess_what = (1)
        print(type(guess_what))

    def dictionaries():

        empty_dict = {}
        empty_dict = dict()

        collections_map = {
            'mutable': ['list', 'set', 'dict'],
            'immutable': ['tuple', 'frozenset']
        }

        print(collections_map['immutable'])
        print(collections_map.get('irresistible', 'not found'))

        print('mutable' in collections_map)  # searching key in dict need constant time!

        beatles_map = {
            'Paul': 'Bass',
            'John': 'Guitar',
            'George': 'Guitar',
        }

        print(beatles_map)
        beatles_map['Ringo'] = 'Drums'
        print(beatles_map)

        del beatles_map['John']
        print(beatles_map)

        beatles_map.update({
            'John': 'Guitar'
        })
        print(beatles_map)

        print(beatles_map.pop('Ringo'))
        print(beatles_map)

        unknown_dict = {}
        print(unknown_dict.setdefault('key', 'default'))
        print(unknown_dict)
        print(unknown_dict.setdefault('key', 'new_default'))

        for key in collections_map:
            print(key)

        for key, value in collections_map.items():
            print('{} - {}'.format(key, value))

        for value in collections_map.values():
            print(value)

        from collections import OrderedDict

        ordered = OrderedDict()

        for number in range(10):
            ordered[number] = str(number)

        for key in ordered:
            print(key)

    #######################
    def sets():
        # изменяемые, поиск элемента за константное время
        empty_set = set()
        number_set = {1, 2, 3, 3, 4, 5}
        print(number_set)
        print(2 in number_set)

        odd_set = set()
        even_set = set()
        for number in range(10):
            if number % 2:
                odd_set.add(number)
            else:
                even_set.add(number)

        print(odd_set)
        print(even_set)

        # Union of sets
        union_set = odd_set | even_set
        union_set = odd_set.union(even_set)
        print(union_set)

        # Intersection of sets
        intersection_set = odd_set & even_set
        intersection_set = odd_set.intersection(even_set)
        print(intersection_set)

        # difference between sets
        difference_set = odd_set - even_set
        difference_set = odd_set.difference(even_set)
        print(difference_set)

        # symmetric difference between sets
        symmetric_difference_set = odd_set ^ even_set
        symmetric_difference_set = odd_set.symmetric_difference(even_set)
        print(symmetric_difference_set)

        even_set.remove(2)
        print(even_set)

        print(even_set.pop())
        print(even_set)

        frozen = frozenset(['A', 'B', 'C'])  # immutable!
        # frozen.add('O') # Error!

        # Usefull links
        # https://docs.python.org/3/library/stdtypes.html
        # https://docs.python.org/3/tutorial/datastructures.html
        # https://en.wikipedia.org/wiki/Hash_table

    def functions():
        from datetime import datetime

        def get_seconds():
            """Return current seconds"""
            return datetime.now().second

        # print(get_seconds())

        def split_tags(tag_string):
            tag_list = []
            for tag in tag_string.split(','):
                tag_list.append(tag.strip())

            return tag_list

        # print(split_tags('python, coursera, mooc'))

        # Types annotation!
        def add(x: int, y: int) -> int:
            return x + y

        # print(add(10, 11))
        # print(add('still ', 'works'))

        def extender(source_list, extend_list):
            source_list.extend(extend_list)

        # values = [1, 2, 3]
        # extender(values, [4, 5, 6])
        # print(values)

        def replacer(source_tuple, replace_with):
            source_tuple = replace_with

        # user_info = ('Guido', '31/01')
        # replacer(user_info, ('Larry', '27/09'))
        # print(user_info)

        # Named args
        def say(greeting, name):
            print('{} {}'.format(greeting, name))

        # say('Hello', 'Kitty')
        # say(name='Kitty', greeting='Hello')

        # Args by default
        def greeting(name='it\'s me...'):
            print('Hello, {}'.format((name)))

        # greeting()

        def append_one(iterable=[]):
            iterable.append(1)
            return iterable

        # print(append_one([1]))
        # print(append_one()) # [1]
        # print(append_one()) # [1, 1]

        # def function(iterable=None):
        #    if iterable is None:
        #        iterable = []
        # def function(iterable=None):
        #    iterable = iterable or []

        # STARS
        def printer(*args):
            print(type(args))

            for argument in args:
                print(argument)

        # printer(1, 2, 3, 4, 5)
        # name_list = ['John', 'Bill', 'Amy']
        # printer(*name_list)

        def printer(**kwargs):
            print(type(kwargs))

            for key, value in kwargs.items():
                print('{}: {}'.format(key, value))

        # printer(a=10, b=11) # a: 10 / b: 11

        payload = {
            'user_id': 117,
            'feedback': {
                'subject': 'Registration fields',
                'message': 'There is no country for old men'
            }
        }
        # printer(**payload)
        # <class 'dict'>
        # user_id: 117
        # feedback: {'subject': 'Registration fields', 'message': 'There is no country for old men'}

    def files():
        f = open('filename')
        text_model = ['r', 'w', 'a', 'r+']
        binary_modes = ['br', 'bw', 'ba', 'br+']
        f.write('The world is changed.\nI taste it in the water.\n')  # 47
        f.close()
        f.open('filename', 'r+')
        f.read()
        f.tell()  # 47
        f.read()  # ..
        f.seek(0)
        f.tell()  # 0
        print(f.read())  # The world is changed.\n
        f.close()

        f = open('filename', 'r+')
        f.readline()  # 'The world is changed.\n'
        f.close()
        f = open('filename', 'r+')
        f.readlines()  # ['The world is changed.\n','I taste it in the water.\n']
        f.close()

        with open('filename') as f:
            print(f.read())

    def functional_programming():
        def caller(func, params):
            return func(*params)

        def printer(name, origin):
            print('I\'m {} of {}!'.format(name, origin))

        # caller(printer, ['Moana', 'Motunui'])

        def get_multiplier():
            def inner(a, b):
                return a * b

            return inner

        # multiplier = get_multiplier()
        # print(multiplier(10, 11))
        # print(multiplier.__name__)

        def get_multiplier(number):
            def inner(a):
                return a * number

            return inner

        # multiplier_by_2 = get_multiplier(2)
        # print(multiplier_by_2(10))

        #######################################################
        # map, filter, lambda
        def squarify(a):
            return a ** 2

        # print(list(map(squarify, range(5)))) # [0, 1, 4, 9, 16]
        # OLD STYLE:
        squared_list = []
        for number in range(5):
            squared_list.append(squarify(number))

        # print(squared_list) # [0, 1, 4, 9, 16]

        def is_positive(a):
            return a > 0

        # print(list(filter(is_positive, range(-2, 3))))
        # OLD STYLE:
        positive_list = []
        for number in range(-2, 3):
            if is_positive(number):
                positive_list.append(number)

        # print(positive_list)
        # LAMBDA-function
        # print(list(map(lambda x: x ** 2, range(5))))
        # print(list(filter(lambda  x: x > 0, range(-2, 3))))
        def stringify_list(num_list):
            return list(map(str, [1, 2, 3]))

        # print(stringify_list(range(10)))

        # FUNCTOOLS
        def multiply(a, b):
            return a * b

        # print(reduce(multiply, [1, 2, 3, 4, 5]))
        # print(reduce(lambda x, y: x * y, range(1, 6)))
        from functools import partial
        def greeter(person, greeting):
            return '{}, {}!'.format(greeting, person)

        hier = partial(greeter, greeting='Hi')
        helloer = partial(greeter, greeting='Hello')
        # print(hier('brother'))
        # print(helloer('sir'))

        # Create List
        # print([number ** 2 for number in range(10)])
        # print([num for num in range(10) if num % 2 == 0])
        # Create Dict
        # print({number: number ** 2 for number in range(5)})

        # print({num % 10 for num in range(100)})
        num_list = range(7)
        squared_list = [x ** 2 for x in num_list]
        print(list(zip(num_list, squared_list)))
        # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]

    def decorators():
        """
        def decorator(func):
            return func
        @decorator
        def decorated():
            print('Hello!')
        decorated = decorator(decorated)
        """
        """
        def decorator(func):
            def new_func():
                pass
            return new_func

        @decorator
        def decorated():
            print('Hello!')
        decorated()
        print(decorated.__name__)
        """
        """
        # Need decorator that writes result of decorated function to log
        
        import functools
        def logger(func):
            @functools.wraps(func)
            def wrapped(*args, **kwargs):
                result = func(*args, **kwargs)
                with open('log.txt','w') as f:
                    f.write(str(result))

                return result
            return wrapped

        @logger
        def summator(num_list):
            return sum(num_list)
        print('Summator: {}'.format(summator([1, 2, 3, 4, 5])))
        with open('log.txt', 'r') as f:
            print('log.txt: {}'.format(f.read()))
        print(summator.__name__)
        """
        """
        # Need decorator with param, which writes log to specified file
        
        def logger(filename):
            def decorator(func):
                def wrapped(*args, **kwargs):
                    result = func(*args, **kwargs)
                    with open(filename, 'w') as f:
                        f.write(str(result))
                    return result
                return wrapped
            return decorator

        @logger('new_log.txt')
        def summator(num_list):
            return sum(num_list)

        print('Summator: {}'.format(summator([1, 2, 3, 4, 5, 6])))
        with open('new_log.txt', 'r') as f:
            print('new_log.txt: {}'.format(f.read()))
        """

        """
        If we use many decorators?
        
        def first_decorator(func):
            def wrapped():
                print('Inside first_decorator product')
                return func()
            return wrapped
        def second_decorator(func):
            def wrapped():
                print('Inside second_decorator product')
                return func()
            return wrapped

        @first_decorator
        @second_decorator
        def decorated():
            print('Finally called...')
        # decorated = first_decorator(second_decorator(decorated))
        decorated()
        #Inside first_decorator product
        #Inside second_decorator product
        #Finally called...
        """

        def bold(func):
            def wrapped():
                return "<b>" + func() + "</b>"

            return wrapped

        def italic(func):
            def wrapped():
                return "<i>" + func() + "</i>"

            return wrapped

        @bold
        @italic
        def hello():
            return "hello world"

        # hello = bold(italic(hello))
        print(hello())
        # <b><i>hello world</i></b>

    def generators():
        def even_range(start, end):
            current = start
            while current < end:
                yield current
                current += 2

        # for number in even_range(0, 10):
        #    print(number)
        ranger = even_range(0, 4)

        # print(next(ranger))
        # print(next(ranger))

        def list_generator(list_obj):
            for item in list_obj:
                yield item
                print('After yielding {}'.format(item))

        generator = list_generator([1, 2])

        # print(next(generator))
        # print(next(generator))

        def fibonacci(number):
            a = b = 1
            for _ in range(number):
                yield a
                a, b = b, a + b

        # for num in fibonacci(10):
        #    print(num)

        def accumulator():
            total = 0
            while True:
                value = yield total
                print('Got: {}'.format(value))

                if not value: break
                total += value

        generator = accumulator()
        print(next(generator))

        print('Accumulated: {}'.format(generator.send(1)))
        print('Accumulated: {}'.format(generator.send(5)))
        print('Accumulated: {}'.format(generator.send(4)))

        # Туториал по функциям из документации
        # https://docs.python.org/3/tutorial/controlflow.html#defining-functions

        # Работа с файлами
        # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

        # Встроенные функции
        # https://docs.python.org/3/library/functions.html

        # Сортировка
        # https://docs.python.org/3/howto/sorting.html

        # Функциональное программирование
        # https://docs.python.org/3/howto/functional.html

        # Модуль functools
        # https://docs.python.org/3/library/functools.html

        # Декораторы
        # http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html

    generators()


def week_3():
    # num = 13
    # print(isinstance(num, int))
    class Human:
        pass

    class Robot:
        """Instead pass we use some docs"""

    # print(Robot)
    # print(dir(Robot))
    class Planet:
        pass

    planet = Planet()
    # print(planet)
    solar_system = []
    for i in range(8):
        planet = Planet()
        solar_system.append(planet)
    # print(solar_system)
    solar_system = {}
    for i in range(8):
        planet = Planet()
        solar_system[planet] = True

    # print(solar_system)

    class Planet:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

        def __repr__(self):
            return f"Planet {self.name}"

    earth = Planet("Earth")
    # print(earth.name) #Earth
    # print(earth) # with __str__ => Earth

    solar_system = []
    planet_names = [
        "Mercury", "Venus", "Earth", "Mars",
        "Jupyter", "Saturn", "Uranus", "Neptune"
    ]

    for name in planet_names:
        planet = Planet(name)
        solar_system.append(planet)
    # print(solar_system) # [<__main__.week_3.<locals>.Planet object at 0x034FDA70>, <__main__.week_3.<locals>.Planet object at 0x034FDB90>, <__main__.week_3.<locals>.Planet object at 0x034FDA50>, <__main__.week_3.<locals>.Planet object at 0x034FD9D0>, <__main__.week_3.<locals>.Planet object at 0x034FDAB0>, <__main__.week_3.<locals>.Planet object at 0x034FDC10>, <__main__.week_3.<locals>.Planet object at 0x034FDC30>, <__main__.week_3.<locals>.Planet object at 0x034FDC50>]
    # with __repr__ => [Planet Mercury, Planet Venus, Planet Earth, Planet Mars, Planet Jupyter, Planet Saturn, Planet Uranus, Planet Neptune]

    mars = Planet("Mars")
    # print(mars) # Planet Mars
    # print(mars.name) # 'Mars'

    mars.name = "Second Earth?"
    # print(mars.name) # 'Second Earth?'
    # del mars.name => delete attribute!

    ##### Attributes for class
    class Planet:
        """Some description for class Planet"""
        count = 0

        def __init__(self, name, population=None):
            self.name = name
            self.population = population or []
            Planet.count += 1

    earth = Planet("Earth")
    mars = Planet("Mars")

    # print(Planet.count) #2
    # print(mars.count) #2

    # destructors for class
    class Human:

        def __del__(self):
            print("Goodbye!")

    # human = Human()
    # del human # Goodbye!
    planet = Planet("Earth")

    # print(planet.__dict__) # {'name': 'Earth', 'population': []}
    # planet.mass = 5.97e24
    # print(planet.__dict__)  # {'name': 'Earth', 'population': [], 'mass': 5.97e+24}
    # print(Planet.__dict__) # {'__module__': '__main__', '__doc__': 'Some description for class Planet', 'count': 3, '__init__': <function week_3.<locals>.Planet.__init__ at 0x015FCA50>, '__dict__': <attribute '__dict__' of 'Planet' objects>, '__weakref__': <attribute '__weakref__' of 'Planet' objects>}
    # print(Planet.__doc__) # Some description for class Planet
    # print(dir(planet)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'count', 'name', 'population']
    # print(planet.__class__) # <class '__main__.week_3.<locals>.Planet'>

    # constructor class unit
    class Planet:

        def __new__(cls, *args, **kwargs):
            print("__new__ called")
            obj = super().__new__(cls)
            return obj

        def __init__(self, name):
            print("__init__ called")
            self.name = name

    # planet = Planet("Earth")
    # == planet = Planet.__new__(Planet, "Earth")
    # if isinstance(planet, Planet):
    #     Planet.__init__(planet, "Earth")

    # METHODS
    class Human:

        def __init__(self, name, age=0):
            self.name = name
            self.age = age

    class Planet:

        def __init__(self, name, population=None):
            self.name = name
            self.population = population or []

        def add_human(self, human):
            print(f"Welcome to {self.name}, {human.name}!")
            self.population.append(human)

    mars = Planet("Mars")
    bob = Human("Bob")

    # mars.add_human(bob)
    # print(mars.population)
    ######### CALL methods from methods
    class Human:
        def __init__(self, name, age=0):
            self._name = name
            self._age = age

        def _say(self, text):
            print(text)

        def say_name(self):
            self._say(f"Hello, I am {self._name}")

        def say_how_old(self):
            self._say(f"I am {self._age} years old")

    bob = Human("Bob", age=29)

    # bob.say_name()
    # bob.say_how_old()

    # NOT RECOMMENDED print(bob._name) or bob._say("Whatever we want")

    # Class method (@classmethod)
    class Event:

        def __init__(self, description, event_date):
            self.description = description
            self.date = event_date

        def __str__(self):
            return f"Event \"{self.description}\" at {self.date}"

    from datetime import date

    event_description = "Рассказать, что такое @classmethod"
    event_date = date.today()

    event = Event(event_description, event_date)

    # print(event) # Event "Рассказать, что такое @classmethod" at 2018-08-04

    def extract_description(user_string):
        return "открытие чемпионата мира по футболу"

    def extract_date(user_string):
        return date(2018, 6, 14)

    class Event:

        def __init__(self, description, event_date):
            self.description = description
            self.date = event_date

        def __str__(self):
            return f"Event \"{self.description}\" at {self.date}"

        @classmethod
        def from_string(cls, user_input):
            description = extract_description(user_input)
            date = extract_date(user_input)
            return cls(description, date)

    event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
    # print(event) # Event "открытие чемпионата мира по футболу" at 2018-06-14

    # classmethod inside library:
    # print(dict.fromkeys("12345")) # {'1': None, '2': None, '3': None, '4': None, '5': None}

    #### Static method of class (@staticmethod)
    class Human:

        def __init__(self, name, age=0):
            self.name = name
            self.age = age

        @staticmethod
        def is_age_valid(age):
            return 0 < age < 150

    # print(Human.is_age_valid(35)) # True
    # human = Human("Old Bobby")
    # print(human.is_age_valid(234)) # False

    ### Calculated property of class
    class Robot:

        def __init__(self, power):
            self.power = power

    wall_e = Robot(100)
    wall_e.power = 200

    # print(wall_e.power) # 200
    # if we not want to set negative power to robot:
    class Robot:

        def __init__(self, power):
            self._power = power

        power = property()

        @power.setter
        def power(self, value):
            if value < 0:
                self._power = 0
            else:
                self._power = value

        @power.getter
        def power(self):
            return self._power

        @power.deleter
        def power(self):
            print("make robot useless")
            del self._power

    wall_e = Robot(100)
    wall_e.power = -20

    # print(wall_e.power)
    # del wall_e.power # make robot useless

    class Robot:

        def __init__(self, power):
            self._power = power

        @property
        def power(self):
            # Здесь могут быть любые полезные вычисления
            return self._power

    wall_e = Robot(100)
    # print(wall_e.power)

    # Example for weather forecasting for the city

    # usefull links
    # Описание классов в документации Python 3.
    # https://docs.python.org/3.6/tutorial/classes.html

    # Очень хорошая вводная статья на английском про классы.
    # http://www.python-course.eu/python3_object_oriented_programming.php

    # Также с того же ресурса статья с примерами про атрибуты,  @classmethod @staticmethod.
    # http://www.python-course.eu/python3_class_and_instance_attributes.php

    # И там же про @ property.
    # http://www.python-course.eu/python3_properties.php

    # На русском языке хорошая статья нашлась на Wikipedia.
    # https://ru.wikipedia.org/wiki/Объектно-ориентированное_программирование_на_Python

    # Обратите внимание, что помимо основ она содержит материалы, которые мы подробно осветим далее в курсе.

    ########################################################################################
    # Наследование классов
    class Pet:
        def __init__(self, name=None):
            self.name = name

    class Dog(Pet):
        def __init__(self, name, breed=None):
            super().__init__(name)
            self.breed = breed

        def say(self):
            return "{0}: waw".format(self.name)

    dog = Dog("Шарик", "Доберман")
    # print(dog.name)
    # print(dog.say())

    # Multiple inherited class

    class ExportJSON:
        def to_json(self):
            return json.dumps({
                "name": self.name,
                "breed": self.breed
            })

    class ExDog(Dog, ExportJSON):
        pass

    dog = ExDog("Белка", breed="Дворняжка")

    # print(dog.to_json()) # {"name": "\u0411\u0435\u043b\u043a\u0430", "breed": "\u0414\u0432\u043e\u0440\u043d\u044f\u0436\u043a\u0430"}

    # isinstance(dog, Dog) #True
    # issubclass(Dog, Pet)

    # Method Resolution Order
    # print(ExDog.__mro__) # (<class '__main__.week_3.<locals>.ExDog'>, <class '__main__.week_3.<locals>.Dog'>, <class '__main__.week_3.<locals>.Pet'>, <class '__main__.week_3.<locals>.ExportJSON'>, <class 'object'>)

    class ExDog(Dog, ExportJSON):
        def __init__(self, name, breed=None):
            # вызов медота по MRO
            super().__init__(name, breed)
            # super(ExDog, self).__init__(name)

    class WoolenDog(Dog, ExportJSON):
        def __init__(self, name, breed=None):
            # явное указание метода конкретного класса
            super(Dog, self).__init__(name)
            self.breed = "Шерстяная собака породы {0}".format(breed)

    dog = WoolenDog("Жучка", breed="Такса")
    # print(dog.breed) # Шерстяная собака породы Такса

    # Conflicts of naming, name mangling
    class Dog(Pet):
        def __init__(self, name, breed=None):
            super().__init__(name)
            self.__breed = breed

        def say(self):
            return "{0} waw!".format(self.name)

        def get_breed(self):
            return self.__breed

    class ExDog(Dog, ExportJSON):
        def get_breed(self):
            return "порода: {0} - {1}".format(self.name, self.__breed)

    dog = ExDog("Фокс", "Мопс")

    # print(dog.__dict__) # {'name': 'Фокс', '_Dog__breed': 'Мопс'}
    # print(dog.get_breed()) # Error: AttributeError: 'ExDog' object has no attribute '_ExDog__breed'

    class ExportJSON:
        def to_json(self):
            pass

    class ExDog(Dog, ExportJSON):
        def get_breed(self):
            return "порода: {0} - {1}".format(self.name, self._Dog__breed)

    dog = ExDog("Фокс", "Мопс")
    # print(dog.get_breed()) # порода: Фокс - Мопс

    ################################
    # Class composition
    class ExportXML:
        def to_xml(self):
            pass

    class ExDog(Dog, ExportJSON, ExportXML):
        pass

    dog = ExDog("Фокс", "мопс")
    dog.to_xml()
    dog.to_json()

    #########
    import json

    class PetExport:
        def export(self, dog):
            raise NotImplementedError

    class ExportJSON(PetExport):
        def export(self, dog):
            return json.dumps({
                "name": dog.name,
                "breed": dog.breed
            })

    class ExportXML(PetExport):
        def export(self, dog):
            return """<?xml version="1.0" encoding="utf-8?>
            <dog>
                <name>{0}</name>
                <breed>{1}</breed>
            </dog>
            """.format(dog.name, dog.breed)

    class Pet:
        def __init__(self, name):
            self.name = name

    class Dog(Pet):
        def __init__(self, name, breed=None):
            super().__init__(name)
            self.breed = breed

    class ExDog(Dog):
        def __init__(self, name, breed=None, exporter=None):
            super().__init__(name, breed=None)
            self._exporter = exporter or ExportJSON()
            if not isinstance(self._exporter, PetExport):
                raise ValueError("bad exporter", exporter)

        def export(self):
            return self._exporter.export(self)

    dog = ExDog("Шарик", "Дворняга", exporter=ExportXML())
    # print(dog.export()) # <?xml version="1.0" encoding="utf-8?><dog><name>Шарик</name><breed>None</breed></dog>
    dog = ExDog("Шарик", "Дворняга")
    # print(dog.export()) # {"name": "\u0428\u0430\u0440\u0438\u043a", "breed": null}

    # Наследование классов в python
    # https://docs.python.org/3/tutorial/classes.html#inheritance

    #######################
    # Exceptions
    # Hierarchy of exceptions
    # BaseException
    #   +-- SystemExit
    #   +-- KeyboardInterrupt
    #   +-- GeneratorExit
    #   +-- Exception
    #       +-- StopIteration
    #       +-- AssertionError
    #       +-- AttributeError
    #       +-- LookupError
    #           +-- IndexError
    #           +-- KeyError
    #       +-- OSError
    #       +-- SystemError
    #       +-- TypeError
    #       +-- ValueError

    """
    class MyClass():
        pass
    obj = MyClass()
    obj.foo
    Traceback (most recent call last):
      File "E:\Work\Learning\python\venv\lib\site-packages\IPython\core\interactiveshell.py", line 2963, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-3-e6020928e2ca>", line 1, in <module>
        obj.foo
    AttributeError: 'MyClass' object has no attribute 'foo'
    
    d = {"foo": 1}
    d["bar"]
    Traceback (most recent call last):
      File "E:\Work\Learning\python\venv\lib\site-packages\IPython\core\interactiveshell.py", line 2963, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-5-586c1efcf0c1>", line 1, in <module>
        d["bar"]
    KeyError: 'bar'
    
    l = [1,2]
    l[10]
    Traceback (most recent call last):
      File "E:\Work\Learning\python\venv\lib\site-packages\IPython\core\interactiveshell.py", line 2963, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-7-f97e037cfd13>", line 1, in <module>
        l[10]
    IndexError: list index out of range
    
    int("asdf")
    Traceback (most recent call last):
      File "E:\Work\Learning\python\venv\lib\site-packages\IPython\core\interactiveshell.py", line 2963, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-8-84b8a2bb8310>", line 1, in <module>
        int("asdf")
    ValueError: invalid literal for int() with base 10: 'asdf'
    
    1 + "1"
    Traceback (most recent call last):
      File "E:\Work\Learning\python\venv\lib\site-packages\IPython\core\interactiveshell.py", line 2963, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-9-b780703cc5f9>", line 1, in <module>
        1 + "1"
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """

    ###########
    # Exception handling
    def exception_handling_simple():
        try:
            1 / 0
        except:
            print("Ошибка")

    # bad example of handling every type of exception
    def exception_handling_bad():
        try:
            1 / 0
        except Exception:
            print("Ошибка")

    # It's better to handling exact type of exception
    def exception_handling_exact_type_error():
        while True:
            try:
                raw = input("введите число: ")
                number = int(raw)
                break
            except ValueError:
                print("некорректное значение")

    # Use Else if try/except
    def exception_handling_with_else():
        while True:
            try:
                raw = input("введите число: ")
                number = int(raw)
                break
            except ValueError:
                print("некорректное значение")
            else:
                break

    # Handling several exceptions
    def exception_handling_several_errors():
        while True:
            try:
                raw = input("введите число: ")
                number = int(raw)
                break
            except ValueError:
                print("некорректное значение")
            except KeyboardInterrupt:
                print("выход")
                break

    def exception_handling_several_errors_with_same_code():
        total_count = 100_000
        while True:
            try:
                raw = input("введите число: ")
                number = int(raw)
                total_count = total_count / number
                break
            except (ValueError, ZeroDivisionError):
                print("некорректное значение!")

    # Inherited exceptions
    def exception_handling_hierarchy():
        database = {
            "red": ["fox", "flower"],
            "green": ["peace", "M", "python"]
        }

        try:
            color = input("введите цвет: ")
            number = input("введите номер по порядку: ")

            label = database[color][int(number)]
            print("вы выбрали: ", label)
        # except (IndexError, KeyError):
        except LookupError:
            print("Объект не найден")

    def exception_handling_with_finally():
        f = open("/etc/hosts")
        try:
            for line in f:
                print(line.rstrip("\n"))
                1 / 0

        except OSError:
            print("ошибка")
        finally:
            f.close()

    # Exceptions generating
    def get_access_to_exception_object():
        try:
            with open("/file/not/found") as f:
                content = f.read()
        except OSError as err:
            print(err.errno, err.strerror)

    def get_access_to_exception_object_with_args():
        import os.path

        filename = "/file/not/found"
        try:
            if not os.path.exists(filename):
                raise ValueError("файл не существует", filename)
        except ValueError as err:
            message, code = err.args[0], err.args[1]
            print(message, code)

    def get_access_to_exception_stack():
        import traceback

        try:
            with open("/file/not/found") as f:
                content = f.read()
        except OSError as err:
            trace = traceback.print_exc()
            print(trace)

    def raise_exception():
        try:
            raw = input("введите число: ")
            if not raw.isdigit():
                raise ValueError
        except ValueError:
            print("некорректное значение!")

    def raise_exception_extended():

        try:
            raw = input("введите число: ")
            if not raw.isdigit():
                raise ValueError("плохое число", raw)
        except ValueError as err:
            print("некорректное значение!", err.args[0], err.args[1])

    def raise_from_exception():

        try:
            raw = input("введите число: ")
            if not raw.isdigit():
                raise ValueError("плохое число", raw)
        except ValueError as err:
            print("ошибка: ", err.args[0], err.args[1])

            raise TypeError("ошибка") from err

    def using_assert():
        assert 1 == 0, "1 not equal 0"  # AssertionError: 1 not equal 0

    # Using flag -O turning OFF all assertion error!
    def using_assert2(id):
        assert isinstance(id, int), "id must be int"
        print("выполняем поиск")

    # using_assert2("foo")
    # python lessons.py => using_assert2("foo") => AssertionError: id must be int
    # python -O lessons.py => using_assert2("foo") => выполняем поиск

    # Performance of exceptions
    def performance_of_exceptions():
        # %%timeit
        my_dict = {"foo": 1}
        for _ in range(1000):
            try:
                my_dict["bar"]
            except KeyError:
                pass

    def performance_of_exceptions2():
        # %%timeit
        my_dict = {"foo": 1}
        for _ in range(1000):
            if "bar" in my_dict:
                _ = my_dict["bar"]

    # performance_of_exceptions() # 1000 loops, best of 3: 511 mks per loop
    # performance_of_exceptions2()  # 1000 loops, best of 3: 78 mks per loop

    ###########################
    # Exceptions in requests
    # import requests
    # print(requests.__file__)
    # venv\lib\site-packages\requests\__init__.py => venv\lib\site-packages\requests\exceptions.py
    # HTTPError, SSLError,...

    def requests_exceptions(url):
        import requests

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.Timeout:
            print('ошибка timeout, url', url)
        except requests.HTTPError as err:
            code = err.response.status_code
            print(f'ошибка url: {url}, code: {code}')
        except requests.RequestException:
            print('ошибка скачивания url: ', url)
        else:
            print(response.content)

    # requests_exceptions('https://github.com') # OK
    # requests_exceptions('https://notfound-github.com')  # ошибка скачивания url:  https://notfound-github.com
    # requests_exceptions('http://github.com/not_found')  # ошибка url: http://github.com/not_found, code: 404

    # Обработка ошибок, исключения в python
    # https://docs.python.org/3.6/tutorial/errors

    # Built-in exceptions
    # https://docs.python.org/3/library/exceptions.html


def week_4():
    def magic_methods():
        class User:
            def __init__(self, name, email):
                self.name = name
                self.email = email

            def get_email_data(self):
                return {
                    'name': self.name,
                    'email': self.email
                }

        jane = User('Jane Doe', 'janedoe@example.com')

        # print(jane.get_email_data())

        class Singleton:
            instance = None

            def __new__(cls):
                if cls.instance is None:
                    cls.instance = super().__new__(cls)
                return cls.instance

        a = Singleton()
        b = Singleton()

        # print(a is b)

        class User:
            def __init__(self, name, email):
                self.name = name
                self.email = email

            def __str__(self):
                return f'{self.name} <{self.email}>'

        jane = User('Jane Doe', 'janedoe@example.com')

        # print(jane)

        class User:
            def __init__(self, name, email):
                self.name = name
                self.email = email

            def __hash__(self):
                return hash(self.email)

            def __eq__(self, obj):
                return self.email == obj.email

        jane = User('Jane Doe', 'jdoe@example.com')
        joe = User('Joe Doe', 'jdoe@example.com')

        # print(jane == joe) # __eq__ => True!

        # __getattr__, __getattribute__
        # __setattr__, __delattr__

        class Researcher:
            def __getattr__(self, name):
                return 'Nothing found :('

            def __getattribute__(self, name):
                return 'nope'

        obj = Researcher()

        # print(obj.attr) # nope
        # print(obj.method) # nope
        # print(obj.DDSDFSDFSDF) # nope

        # __setattr__ => create event on setting attr

        class Polite:
            def __delattr__(self, name):
                value = getattr(self, name)
                print(f'Goodbye {name}, you were {value}!')

                object.__delattr__(self, name)

        obj = Polite()
        obj.attr = 10
        # del obj.attr # => Goodbye attr, you were 10!

        class Logger:
            def __init__(self, filename):
                self.filename = filename

            def __call__(self, func):
                def wrapped(*args, **kwargs):
                    with open(self.filename, 'a') as f:
                        f.write('Oh Danny boy...')

                    return func(*args, *kwargs)

                return wrapped

        # logger = Logger('log.txt')

        # @logger
        # def completely_useless_function():
        #     pass

        # completely_useless_function()

        # with open('log.txt') as f:
        #    print(f.read())

        # Магический метод call используется при вызове экземпляра класса,
        # а не самого класса.
        # Однако, если класс с переопределённым методом call является метаклассом
        # (о них мы поговорим чуть позже), то экземпляром этого класса является
        # новый класс. А это значит, что при создании объекта класса,
        # метаклассом которого является класс с переопределённым магическим
        # методом call, вызывается этот самый метод call.
        # Причем вызывается он раньше new и init.

        import random

        class NoisyInt:
            def __init__(self, value):
                self.value = value

            def __add__(self, obj):
                noise = random.uniform(-1, 1)
                return self.value + obj.value + noise

        # a = NoisyInt(10)
        # b = NoisyInt(20)

        # for _ in range(3):
        #    print(a + b)

        # 29.930463632745052
        # 30.96830897108625
        # 29.63950941993512

        class ItemList:
            def __init__(self, original_list=None):
                self.container = original_list or []

            def __getitem__(self, index):
                return self.container[index]

            def __setitem__(self, key, value):
                self.container[index] = value

            def __str__(self):
                return self.container.__str__()

        # numbers = ItemList([1,2,3])
        # print(numbers[2]) # 3

        # numbers[3] = 4
        # print(numbers) # [1,2,3,4]

    # magic_methods()

    def iterators():
        iterator = iter([1, 2, 3])
        print(next(iterator))

    def getSquareIterator():
        class SquareIterator:
            def __init__(self, start, end):
                self.current = start
                self.end = end

            def __iter__(self):
                return self

            def __next__(self):
                if self.current >= self.end:
                    raise StopIteration

                result = self.current ** 2
                self.current += 1
                return result

        for num in SquareIterator(1, 4):
            print(num)

    # getSquareIterator()

    def getIndexIterable():
        class IndexIterable:
            def __init__(self, obj):
                self.obj = obj

            def __getitem__(self, index):
                return self.obj[index]

        for letter in IndexIterable('str'):
            print(letter)

    # getIndexIterable()

    def context_managers():
        # with open(filename, 'a') as f:
        #     f.write('New line')
        class open_file:
            def __init__(self, filename, mode):
                self.f = open(filename, mode)

            def __enter__(self):
                return self.f

            def __exit__(self, *args):
                self.f.close()

        # with open_file('test.log', 'w') as f:
        #     f.write('Inside `open_file` context manager')

        # with open_file('test.log', 'r') as f:
        #     print(f.readlines())

        class supress_exception:
            def __init__(self, exc_type):
                self.exc_type = exc_type

            def __enter__(self):
                return

            def __exit__(self, exc_type, exc_value, traceback):
                if exc_type == self.exc_type:
                    print('Nothing happend')
                    return True

        # with supress_exception(ZeroDivisionError):
        #     really_big_number = 1 / 0  # Nothing happend

        # import contextlib
        # with contextlib.supress(ValueError):
        #     raise ValueError

        import time

        class timer():
            def __init__(self):
                self.start = time.time()

            def current_time(self):
                return time.time() - self.start

            def __enter__(self):
                return self

            def __exit__(self, *args):
                print(f'Elapsed: {self.current_time()}')

        with timer() as t:
            time.sleep(1)
            print(f'Current: {t.current_time()}')
            time.sleep(1)

    # magic methods docs:
    # https://docs.python.org/3/reference/datamodel.html
    # context_managers()

    def descriptors():
        class Descriptor:
            def __get__(self, obj, obj_type):
                print('get')

            def __set__(self, obj, value):
                print('set')

            def __delete__(self, obj):
                print('delete')

        class Class:
            attr = Descriptor()

        # instance = Class()
        # instance.attr # get
        # instance.attr = 10 # set
        # del instance.attr # delete

        class Value:
            def __init__(self):
                self.value = None

            @staticmethod
            def _prepare_value(value):
                return value * 10

            def __get__(self, instance, owner):
                return self.value

            def __set__(self, instance, value):
                self.value = self._prepare_value(value)

        class Class:
            attr = Value()

        # instance = Class()
        # instance.attr = 10

        # print(instance.attr) # 100

        class ImportantValue:
            def __init__(self, amount):
                self.amount = amount

            def __get__(self, instance, owner):
                return self.amount

            def __set__(self, instance, value):
                with open('log.txt', 'a') as f:
                    f.write(str(value))

                self.amount = value

        class Account:
            amount = ImportantValue(100)

        # bobs_account = Account()
        # bobs_account.amount = 150

        # with open('log.txt', 'r') as f:
        #     print(f.read())

        # В bound метод по умолчанию передаётся объект, с которым вызван метод.
        # И именно он и записывается в атрибут self метода класса.

        class Property:
            def __init__(self, getter):
                self.getter = getter

            def __get__(self, obj, obj_type=None):
                if obj is None:
                    return self

                return self.getter(obj)

        class Class:
            @property
            def original(self):
                return 'original'

            @Property
            def custom_sugar(self):
                return 'custom sugar'

            def custom_pure(self):
                return 'custom pure'

            custom_pure = Property(custom_pure)

        # obj = Class()

        # print(obj.original)
        # print(obj.custom_sugar)
        # print(obj.custom_pure)

        class StaticMethod:
            def __init__(self, func):
                self.func = func

            def __get__(self, obj, obj_type=None):
                return self.func

        class ClassMethod:
            def __init__(self, func):
                self.func = func

            def __get__(self, obj, obj_type=None):
                if obj_type is None:
                    obj_type = type(obj)

                def new_func(*args, **kwargs):
                    return self.func(obj_type, *args, **kwargs)

                return new_func

        class Class:
            __slots__ = ['anakin']

            def __init__(self):
                self.anakin = 'the chosen one'

        # obj = Class()
        # obj.luke = 'the chosen too' # => AttributeError!

        # descriptors docs
        # http://www.blog.pythonlibrary.org/2016/06/10/python-201-what-are-descriptors/
    # descriptors()

    def metaclasses():
        NewClass = type('NewClass', (), {})
        # print(NewClass) #<class '__main__.NewClass'>
        # print(NewClass()) #<__main__.NewClass object at 0x012A8330>

        class Meta(type):
            def __new__(cls, name, parents, attrs):
                print(f'Creating {name}')

                if 'class_id' not in attrs:
                    attrs['class_id'] = name.lower()

                return super().__new__(cls, name, parents, attrs)

        # class A(metaclass=Meta): #Creating A
        #    pass

        # print(f'A.class_id: "{A.class_id}"') # A.class_id: "a"

        class Meta(type):
            def __init__(cls, name, bases, attrs):
                print(f'Initializing - {name}')

                if not hasattr(cls, 'registry'):
                    cls.registry = {}
                else:
                    cls.registry[name.lower()] = cls

                super().__init__(name, bases, attrs)

        # class Base(metaclass=Meta): pass #Initializing - Base
        # class A(Base): pass #Initializing - A
        # class B(Base): pass #Initializing - B

        # print(Base.registry) #{'a': <class '__main__.week_4.<locals>.metaclasses.<locals>.A'>, 'b': <class '__main__.week_4.<locals>.metaclasses.<locals>.B'>}
        # print(Base.__subclasses__()) #[<class '__main__.week_4.<locals>.metaclasses.<locals>.A'>, <class '__main__.week_4.<locals>.metaclasses.<locals>.B'>]

        from abc import ABCMeta, abstractmethod

        class Sender(metaclass=ABCMeta):
            @abstractmethod
            def send(self):
                """DO smnth"""

        class Child(Sender):
            pass

        # Child() #need to reinitialize method send! => TypeError: Can't instantiate abstract class Child with abstract methods send

        class Child(Sender):
            def send(self):
                print('Sending')

        # Child() # ok!

        # instead of abstract method better to use raise in non-implemented method! =)
        class PythonWay:
            def send(self):
                raise NotImplementedError

        # Docs
        # Data model
        # https://docs.python.org/3/reference/datamodel.html

        # Descriptors
        # https://docs.python.org/3/howto/descriptor.html
    # metaclasses()

    def debugging():
        import requests
        import re

        def main(site_url, substring):
            # import pdb
            # pdb.set_trace()

            site_code = get_site_code(site_url)
            matching_substrings = get_matching_substrings(site_code, substring)
            print(f'"{substring}" found {len(matching_substrings)} times in {site_url}')

        def get_site_code(site_url):
            if not site_url.startswith('http'):
                site_url = 'http://' + site_url

            return requests.get(site_url).text

        def get_matching_substrings(source, substring):
            return re.findall(substring, source)

        main('mail.ru', 'script')  # "script" found 283 times in mail.ru
        # run from console with debugging:
        # python -m pdb lessons.py

    # debugging()

    def tests():
        import unittest

        class TestPython(unittest.TestCase):
            def test_float_to_int_coercion(self):
                self.assertEqual(1, int(1.0))

            def test_get_empty_dict(self):
                self.assertIsNone({}.get('key'))

            def test_trueness(self):
                self.assertTrue(bool(10))

            def test_integer_division(self):
                self.assertIs(10 / 5, 2)

        # run tests from console:
        # python -m unittest lessons.py

        """(venv) >python -m unittest tests.py
            ..F.
            ======================================================================
            FAIL: test_integer_division (tests.TestPython)
            ----------------------------------------------------------------------
            Traceback (most recent call last):
              File "tests.py", line 14, in test_integer_division
                self.assertIs(10 / 5, 2)
            AssertionError: 2.0 is not 2
            
            ----------------------------------------------------------------------
            Ran 4 tests in 0.001s
            
            FAILED (failures=1)
        """
        """
        import json

        import requests

        class Asteroid:
            BASE_API_URL = 'https://api.nasa.gov/neo/rest/v1/neo/{}?api_key=DEMO_KEY'

            def __init__(self, spk_id):
                self.api_url = self.BASE_API_URL.format(spk_id)

            def get_data(self):
                return requests.get(self.api_url).json()

            @property
            def name(self):
                return self.get_data()['name']

            @property
            def diameter(self):
                return int(self.get_data()['estimated_diameter']['meters']['estimated_diameter_max'])

        apophis = Asteroid(2099942)

        print(f'Name: {apophis.name}')
        print(f'Diameter: {apophis.diameter}m')

        # for using without reading online every-time
        with open('apophis_fixture.txt', 'w') as f:
            f.write(json.dumps(apophis.get_data()))

        import json
        import unittest
        from unittest.mock import patch

        from asteroid import Asteroid

        class TestAsteroid(unittest.TestCase):
            def setUp(self):
                self.asteroid = Asteroid(2099942)

            def mocked_get_data(self):
                with open('apophis_fixture.txt') as f:
                    return json.loads(f.read())

            @patch('asteroid.Asteroid.get_data', mocked_get_data)
            def test_name(self):
                self.assertEqual(self.asteroid.name, '99942 Apophis (2004 MN4)')

            @patch('asteroid.Asteroid.get_data', mocked_get_data)
            def test_diameter(self):
                self.assertEqual(self.asteroid.diameter, 682)
        """
        """(venv) >python -m unittest test_asteroid.py
        Name: 99942 Apophis (2004 MN4)
        Diameter: 682m
        ..
        ----------------------------------------------------------------------
        Ran 2 tests in 0.002s

        OK
        """

        """Документация
        pdb
        https://docs.python.org/3/library/pdb.html
        unittest
        https://docs.python.org/3/library/unittest.html
        unittest.mock
        https://docs.python.org/3/library/unittest.mock.html
        unittest.mock examples
        https://docs.python.org/3/library/unittest.mock-examples.html
        """

    tests()


# week_4()
def week5():
    def simple_process():
        import time
        import os

        pid = os.getpid()

        while True:
            print(pid, time.time())
            time.sleep(2)

        # top
        # ps axu | grep ex1.py
        # ps aux | head -1; ps axu | grep ex1.py
        # sudo strace -p 16112
        # lsof -p 16112
        # 0u, 1w, 2u

    # simple_process()

    def create_subprocess():
        import os

        pid = os.fork()
        if pid == 0:
            while True:
                print("child:", os.getpid())
        else:
            print("parent:", os.getpid())
            os.wait()
        # ps uax | grep lessons.py
        # ps axf | grep lessons.py => to see in tree
        # strace -p 16113

    # create_subprocess()

    def memory_of_subprocess():
        import os

        foo = "bar"

        if os.fork() == 0:
            foo = "baz"
            print("child:", foo)
        else:
            print("parent:", foo)
            os.wait()

    # memory_of_subprocess()
    def files_of_subprocess():
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

    # files_of_subprocess()

    def use_multiprocessing():
        from multiprocessing import Process

        def f(name):
            print("hello", name)

        p = Process(target=f, args=("Bob",))
        p.start()
        p.join()

    # use_multiprocessing()

    def use_hierarachy_multiprocessing():
        from multiprocessing import Process

        class PrintProcess(Process):
            def __init__(self, name):
                super().__init__()
                self.name = name

            def run(self):
                print("hello", self.name)

        p = PrintProcess("Mike")
        p.start()  # запуск процесса
        p.join()  # завершение дочерних процессов

    # use_hierarachy_multiprocessing()

    def simple_thread():
        from threading import Thread

        def f(name):
            print("hello", name)

        th = Thread(target=f, args=("Bob",))
        th.start()
        th.join()

    # simple_thread()

    def simple_thread2():
        from threading import Thread

        class PrintThread(Thread):
            def __init__(self, name):
                super().__init__()
                self.name = name

            def run(self):
                print("hello", self.name)

        th = PrintThread("Mike")
        th.start()
        th.join()

    # simple_thread2()

    def using_threadpoolexecutor():
        from concurrent.futures import ThreadPoolExecutor, as_completed

        def f(a):
            return a * a

        # .shutdown() in exit
        with ThreadPoolExecutor(max_workers=3) as pool:
            results = [pool.submit(f, i) for i in range(10)]

            for future in as_completed(results):
                print(future.result())

    # using_threadpoolexecutor()

    def using_queue():
        from queue import Queue
        from threading import Thread

        def worker(q, n):
            while True:
                item = q.get()
                if item is None:
                    break
                print("process data:", n, item)

        q = Queue(5)
        th1 = Thread(target=worker, args=(q, 1))
        th2 = Thread(target=worker, args=(q, 2))
        th1.start();
        th2.start()

        for i in range(50):
            q.put(i)

        q.put(None);
        q.put(None)
        th1.join();
        th2.join()

    # using_queue()

    def using_blocks():
        import threading

        class Point(object):
            def __init__(self):
                self._mutex = threading.RLock()
                self._x = 0
                self._y = 0

            def get(self):
                with self._mutex:
                    return (self._x, self._y)

            def set(self, x, y):
                with self._mutex:
                    self._x = x
                    self._y = y

    # using_blocks()

    def using_blocks2():
        import threading

        a = threading.RLock()
        b = threading.RLock()

        def foo():
            try:
                a.acquire()
                b.acquire()
            finally:
                a.release()
                b.release()

    # using_blocks2()

    def using_conditions():
        import threading

        class Queue(object):
            def __init__(self, size=5):
                self._size = size
                self._queue = []
                self._mutex = threading.RLock()
                self._empty = threading.Condition(self._mutex)
                self._full = threading.Condition(self._mutex)

            def put(self, val):
                with self._full:
                    while len(self._queue) >= self._size:
                        self._full.wait()

                    self._queue.append(val)
                    self._empty.notify()

            def get(self):
                with self._empty:
                    while len(self._queue) == 0:
                        self._empty.wait()

                    ret = self._queue.pop(0)
                    self._full.notify()
                    return ret

    # using_conditions()

    # Know Global Interpretator's Lock (GIL)
    def cpu_bound_program():
        from threading import Thread
        import time

        def count(n):
            while n > 0:
                n -= 1

        # series run
        t0 = time.time()
        count(100_000_000)
        count(100_000_000)
        print(time.time() - t0)

        # parallel run
        t0 = time.time()
        th1 = Thread(target=count, args=(1000_000_000,))
        th2 = Thread(target=count, args=(1000_000_000,))

        th1.start();
        th2.start()
        th1.join();
        th2.join()
        print(time.time() - t0)

    # cpu_bound_program()

    # Документация
    # python multiprocessing
    # https://docs.python.org/3.6/library/multiprocessing.html
    # threading
    # https://docs.python.org/3.6/library/threading.html
    # concurrent.futures
    # https://docs.python.org/3/library/concurrent.futures.html

    def server_socket():
        # server side
        import socket

        # http://docs.python.org/3/library/socket.html
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 10001))  # max port 65535
        sock.listen(socket.SOMAXCONN)

        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            # process data
            print(data.decode("utf8"))

        conn.close()
        sock.close()

    # server_socket()

    def client_side_socket():
        import socket

        sock = socket.socket()
        sock.connect(("127.0.0.1", 10001))
        sock.sendall("ping".encode("utf8"))
        sock.close()

        # or simple
        sock = socket.create_connection(("127.0.0.1", 10001))
        sock.sendall("ping".encode("utf8"))
        sock.close()

    # client_side_socket()

    def socket_with_context_manager():
        # server
        import socket

        with socket.socket() as sock:
            sock.bind(("", 10001))
            sock.listen()

            while True:
                conn, addr = sock.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(data.decode("utf8"))

        # clent
        import socket

        with socket.create_connection(("127.0.0.1", 10001)) as sock:
            sock.sendall("ping".encode("utf8"))

    # socket_with_context_manager()

    def socket_with_timeout_server():
        import socket

        with socket.socket() as sock:
            sock.bind(("", 10001))
            sock.listen()
            while True:
                conn, addr = sock.accept()
                conn.settimeout(5)  # timeout:= None|0|>0
                with conn:
                    while True:
                        try:
                            data = conn.recv(1024)
                        except socket.timeout:
                            print("close connect by timeout")
                            break

                        if not data:
                            break
                        print(data.decode("utf8"))

    # socket_with_timeout_server()

    def socket_with_timeout_client():
        import socket

        with socket.create_connection(("127.0.0.1", 10001), 5) as sock:
            sock.settimeout(2)
            try:
                sock.sendall("ping".encode("utf8"))
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)

    # socket_with_timeout_client()

    def several_requests_by_threads():
        # обработка нескольких соединений одновременно с помощью потоков
        import socket
        import threading

        def process_request(conn, addr):
            print("connected client:", addr)
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode("utf8"))

        with socket.socket() as sock:
            sock.bind(("", 10001))
            sock.listen()
            while True:
                conn, addr = sock.accept()
                th = threading.Thread(target=process_request, args=(conn, addr))
                th.start()

    # several_requests_by_threads()

    def several_requests_by_processes_and_threads():
        # обработка нескольких соединений одновременно и процессами и потоками
        import socket

        with socket.socket() as sock:
            sock.bind(("", 10001))
            sock.listen()
            while True:
                conn, addr = sock.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(data.decode("utf8"))

    def several_requests_by_processes_and_threads_server():
        def process_request(conn, addr):
            print("connected client:", addr)
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(data.decode("utf8"))

        def worker(sock):
            while True:
                conn, addr = sock.accept()
                print("pid", os.getpid())
                th = threading.Thread(target=process_request, args=(conn, addr))
                th.start()

        import socket
        import multiprocess

        with socket.socket() as sock:
            sock.bind(("", 10001))
            sock.listen()

            workers_count = 3
            workers_list = [multiprocess.Process(target=worker, args=(sock,))
                            for _ in range(workers_count)]

            for w in workers_list:
                w.start()

            for w in workers_list:
                w.join()

    # Сокеты в Python
    # https://docs.python.org/3.6/library/socket.html

    # several_requests_by_processes_and_threads_server()

    def non_blocking_io():
        # неблокирующий ввод/вывод
        import socket
        import select

        sock = socket.socket()
        sock.bind(("", 10001))
        sock.listen()

        conn1, addr = sock.accept()
        conn2, addr = sock.accept()

        conn1.setblocking(0)
        conn2.setblocking(0)

        epoll = select.epoll()
        epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
        epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

        conn_map = {
            conn1.fileno(): conn1,
            conn2.fileno(): conn2
        }

    def infinity_cycle_epoll():
        # цикл обработки событий в epoll
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if event & select.EPOLLIN:
                    data = conn_map[fileno].recv(1024)
                    print(data.decode("utf8"))
                elif event & select.EPOLLOUT:
                    conn_map[fileno].send("ping".encode("utf8"))

        # создание соединения к серверу и передача данных
        import socket
        sock = socket.create_connection(("127.0.0.1", 10001))
        sock.sendall(b"client2")

    def iterators():
        class MyRangeIterator:
            def __init__(self, top):
                self.top = top
                self.current = 0

            def __iter__(self):
                return self

            def __next__(self):
                if self.current >= self.top:
                    raise StopIteration

                current = self.current
                self.current += 1
                return current

        counter = MyRangeIterator(3)
        print(counter)
        for it in counter:
            print(it)

        # debug run = python -m pdb lessons.py
        # iterator - first single iter, next only __next__

    def generators():
        def MyRangeGenerator(top):
            current = 0
            while current < top:
                yield current
                current += 1

        counter = MyRangeGenerator(3)
        print(counter)
        for it in counter:
            print(it)

    # generators()
    # debug run = python -m pdb lessons.py
    # Итератор хранит значения для следующей итерации в self
    # Генератор использует локальные переменные

    def coroutines():
        # сопрограммы
        def grep(pattern):
            print("start grep")
            while True:
                line = yield
                if pattern in line:
                    print(line)

        """
        >>g = grep("python")
        >>next(g) # g.send(None)
        start grep
        >>g.send("golang is better?")
        >>g.send("python is simple!")
        python is simple
        
        генераторы производят значения
        Генератор содержит инструкцию yield выражение
        
        сопрограммы потребляют значения
        Сопрограмма содержит инструкцию yield и ожидает пока кто-то отправит в нее значение при помощи метода send
        """

    def coroutines_exit():
        def grep(pattern):
            print("start grep")
            try:
                while True:
                    line = yield
                    if pattern in line:
                        print(line)
            except GeneratorExit:
                print("stop grep")

    """
        >> g = grep("python")
        >> next(g) # g.send(None)
        start grep
        >> g.send("python is the best!")
        python is the best!
        >> g.close()
        stop grep
    """

    """ # Pass exception to coroutine:
    
        >> g = grep("python")
        >> next(g) # g.send(None)
        start grep
        >> g.send("python is the best!")
        >> g.throw(RuntimeError, "something wrong")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        RuntimeError: something wrong
    """

    def coroutines_pep380():
        # Сопрограммы, yield from PEP 0380
        def grep(pattern):
            print("start grep")
            while True:
                line = yield
                if pattern in line:
                    print(line)

        def grep_python_coroutine():
            g = grep("python")
            yield from g

        """
        >> g = grep_python_coroutine() # is g coroutine?
        >> g
        <generator object grep_python_coroutine at ...>
        >> g.send(None)
        start grep
        >> g.send("python wow!")
        python wow!
        
        """

    def pep380_generators():
        def chain(x_iterable, y_iterable):
            yield from x_iterable
            yield from y_iterable

        def the_same_chain(x_iterable, y_iterable):
            for x in x_iterable:
                yield x

            for y in y_iterable:
                yield y

        """    
        >>> a = [1, 2, 3]
        >>> b = (4,5)
        >>> for x in chain(a, b):
                print(x)
        1
        2
        3
        4
        5
        """

    def use_asyncio():
        import asyncio

        @asyncio.coroutine
        def hello_world():
            while True:
                print("Hello World!")
                yield from asyncio.sleep(1.0)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(hello_world())
        loop.close()

    def use_asyncio_def():
        # asyncio, async def / await; PEP 492 Python3.5
        import asyncio

        async def hello_world():
            while True:
                print("Hello World!")
                await asyncio.sleep(1.0)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(hello_world())
        loop.close()

    def tcp_server_asyncio():
        import asyncio

        @asyncio.coroutine
        def handle_echo(reader, writer):
            data = yield from reader.read(1024)
            message = data.decode()
            addr = writer.get_extra_info("peername")
            print("received %r from %r" % (message, addr))
            writer.close()

        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
        server = loop.run_until_complete(coro)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            pass

        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()

    """
    (venv) >>>python asyncio_tcp_server.py
    received 'ping2' from ('127.0.0.1', 64248)
    received 'ping1' from ('127.0.0.1', 64230)
    
    >>> import socket
    >>> sock = socket.create_connection(("127.0.0.1", 10001))
    >>> sock.send(b"ping1")
    5
    
    >>> import socket
    >>> sock = socket.create_connection(("127.0.0.1", 10001))
    >>> sock.send(b"ping2")
    5
    """

    def asyncio_tcp_client():
        import asyncio

        async def tcp_echo_client(message, loop):
            reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)

            print("send: %r" % message)
            writer.write(message.encode())
            writer.close()

        loop = asyncio.get_event_loop()
        message = "Hello World!"
        loop.run_until_complete(tcp_echo_client(message, loop))
        loop.close()

    def asyncio_future():
        # asyncio.Future, analog of concurrent.futures.Future

        import asyncio

        async def slow_operation(future):
            await asyncio.sleep(1)
            future.set_result("Future is done!")

        loop = asyncio.get_event_loop()
        future = asyncio.Future()
        asyncio.ensure_future(slow_operation(future))

        loop.run_until_complete(future)
        print(future.result())
        # Future is done!
        loop.close()

    def asyncio_task():
        # asyncio.Task, run multiple coroutines

        import asyncio

        async def sleep_task(num):
            for i in range(5):
                print(f"process task: {num} iter: {i}")
                await asyncio.sleep(1)

            return num

        # ensure_future or create task
        loop = asyncio.get_event_loop()

        task_list = [loop.create_task(sleep_task(i)) for i in range(2)]
        loop.run_until_complete(asyncio.wait(task_list))
        """
        loop.run_until_complete(loop.create_task(sleep_task(3)))
        # or 
        loop.run_until_complete(asyncio.gather(
            sleep_task(10),
            sleep_task(20),
        ))
        """
        loop.close()

        """
        * из объектов типа asyncio.Future можно создавать цепочки и 
        дожидаться их выполнения в asyncio event loop
        
        * объект типа asyncio.Task хранит в себе связанную корутину и 
        содержит статус ее выполнения
        """

    def asyncio_run_in_executor():
        # loop.run_in_executor, run in separate thread

        import asyncio
        from urllib.request import urlopen

        # a synchronous function
        def sync_get_url(url):
            return urlopen(url).read()

        async def load_url(url, loop=None):
            future = loop.run_in_executor(None, sync_get_url, url)
            response = await future
            print(len(response))

        loop = asyncio.get_event_loop()
        loop.run_until_complete(load_url("https://google.com", loop=loop))
        loop.close()

    """
    Документация
    Модуль select
    https://docs.python.org/3.6/library/select.html
    
    Делегирование вызова генератора pep-0380
    https://www.python.org/dev/peps/pep-0380/
    
    Asyncio
    https://docs.python.org/3.6/library/asyncio.html
    
    Примеры для asyncio
    https://habrahabr.ru/post/217143/
    """

week5()
