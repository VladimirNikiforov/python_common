import socket
import time

class ClientError(BaseException):
    def __init__(self, err):
        self.err = err

class Client:
    def __init__(self, ip, port, timeout=None):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.ip, self.port), self.timeout)

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        #self.sock.settimeout(self.timeout)
        self.sock.sendall(f"put {key} {value} {timestamp}\n".encode("utf8"))
        data = self.sock.recv(1024)
        if data != b"ok\n\n":
            raise ClientError('error')

    def get(self, key):
        self.sock.sendall(f"get {key}\n".encode("utf8"))
        data = self.sock.recv(1024)
        if data == b"ok\n\n":
            return {}
        if data.startswith(b'ok\n'):
            j = data.decode("utf8").lstrip('ok\n').rstrip('\n\n').split('\n')
            d = {}
            for x in j:
                key, r, l = x.split(' ')
                if key in d:
                    d[key].append((float(l), float(r)))
                else:
                    d[key] = [(float(l), float(r))]
            return d
        else:
            raise ClientError('error')