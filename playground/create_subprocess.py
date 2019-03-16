import os

pid = os.fork()
if pid == 0:
    while True:
        print("child:", os.getpid())
else:
    print("parent:", os.getpid())
    os.wait()
