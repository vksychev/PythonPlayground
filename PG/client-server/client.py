import time
import socket
import ast


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def __str__(self):
        return 'host: {}, port: {} , timeout: {}'. \
            format(self.host, self.port, self.timeout)

    def put(self, name, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        request = 'put {} {} {}\n'.format(name, value, timestamp)
        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            try:
                sock.send(request.encode("utf8"))
                req = sock.recv(1024).decode("utf8")[:5]
                print(req)
                if req == 'error':
                    raise ClientError
            except Exception:
                raise ClientError

    def get(self, name):
        request = 'got {}\n'.format(name)
        with socket.create_connection((self.host, self.port), timeout=self.timeout) as sock:
            try:
                sock.sendall(request.encode("utf8"))
                data = sock.recv(1024).decode("utf8")
                return data
                result = dict()
                if data[:5] == 'error':
                    raise ClientError
                data = data.replace('ok\n\n', '').replace('ok\n', '').replace('\n\n', '')
                if data == '':
                    return result
                for s in data.split('\n'):
                    req = s.split(' ')
                    if req[0] in result:
                        result[req[0]].append((int(req[2]), float(req[1])))
                    else:
                        result[req[0]] = [(int(req[2]), float(req[1]))]
                return result

            except Exception:
                raise ClientError


if __name__ == "__main__":
    client = Client("127.0.0.1", 8888, timeout=10)
    client.put("test", 0.5, timestamp=1)
    client.put("test", 2.0, timestamp=2)
    client.put("test", 0.5, timestamp=3)
    client.put("load", 3, timestamp=4)
    client.put("load", 4, timestamp=5)
    print(client.get("test"))
