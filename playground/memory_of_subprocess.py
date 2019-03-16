import os

foo = "bar"

if os.fork() == 0:
    foo = "baz"
    print("child:", foo)
else:
    print("parent:", foo)
    os.wait()
