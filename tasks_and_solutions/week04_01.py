import tempfile
import os

class File:

    def __init__(self, filepath):
        self.filepath = filepath

    def write(self, str):
        with open(self.filepath, 'a') as f:
            f.write(str)

    def __add__(self, obj):
        newfile = os.path.join(tempfile.gettempdir(), 'new.txt')
        print(newfile)
        with open(newfile, 'w') as f1, open(self.filepath, 'r') as f2, open(obj.filepath, 'r') as f3:
            str = ''.join(f2.readlines()) + ''.join(f3.readlines())
            f1.write(str)
        return File(newfile)

    def __getitem__(self, index):
        with open(self.filepath, 'r') as f:
            str = f.readlines()[index]
        return str

    def __str__(self):
        return self.filepath.__str__()

#obj = File('file.txt')
#obj.write('line\n')
#first = File('first.txt')
#first.write('line1\n')
#first.write('line2\n')
#second = File('second.txt')
#second.write('line3\n')
#second.write('line4\n')

#new_obj = first + second
#for line in new_obj:
#  print(line)


"""
Решение
В этом задании нужно было аккуратно реализовать несколько классических 
магических методов и пару обычных. При инициализации мы сохраняем путь, 
а также можем проверить существование файла, хотя это и не требовалось при тестировании. 
Методы write и read просто работают с файлом в системе. 
Хотя наличие метода для чтения не требовалось, его реализация помогает нам 
в работе других функций, да и вообще — какой write без read.

Метод __str__ вряд ли вызвал у вас проблемы, остальные методы более интересны. 
При сложении файлов на нас ложится задача выбора имени нового файла. 
В условии про именование ничего не сказано, и в реальных задачах почти всегда 
над такими деталями приходится думать самостоятельно. 
В примере мы генерим имя с помощью модуля uuid, который позволяет создавать
идентификаторы UUID. Файл мы сохраняем в той же директории, что и существующий, 
что помогает избежать проблем с правами (можно использовать gettempdir как в условии).

При итерации главным вопросом является сохранение номера прочитанной строки. 
Самым простым вариантом было бы просто вернуть итератор строк, например, с помощью 
метода readlines. Однако, в таком случае мы читаем сразу весь файл, который может 
быть очень большим и который весь нам может быть и не нужен. 
В нашем решении мы сохраняем текущую позицию в файле с помощью метода tell и 
используем readline для получения единственной следующей строки. 
По окончании чтения файла метод выбрасывает StopIteration, 
как каждый уважающий себя итератор. 
Можно было также использовать то, что файловый объект в Python сам по себе является 
итератором.
"""

"""
import os
import uuid


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line
"""