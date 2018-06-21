import asyncio

class ClientSocketError(Exception):
    pass

class ClientProtocolError(Exception):
    pass

class Parser:
    ok_response = 'ok\n\n'

    def __init__(self):
        pass

    def parse(self, text, store):
        row = text.replace('\n', '')
        try:
            task = row.split(' ')[0]
            if task == 'put':
                return self._put(row, store)
            elif task == 'get':
                return 'ok\n{}\n'.format(self._get(row,store))
            raise ClientProtocolError
        except Exception:
            raise ClientProtocolError

    def _put(self, row, store):
        task,key, value, timestamp = row.split(' ')
        self.append(key, value, timestamp, store)
        return self.ok_response

    def _get(self, row,store):
        task, key = row.split(' ')
        if key is '*':
            res = ''
            for k in store:
                res += self.get_by_key(k,store)
            return res
        elif key in store:
            return self.get_by_key(key,store)
        else: return('\n')

    def _generate_error(self,name):
        return "error\n{}\n\n".format(name)

    def append(self, key, value, timestamp, store):
        if (value, timestamp) in store[key]:
            return
        if key not in store:
            store[key] = []
        store[key].append(( float(value),int(timestamp)))

    def get_by_key(self,key,store):
        res = ''
        if isinstance(store[key],list):
            for n in store[key]:
                res = res + "{} {} {}\n".format(key, n[0], n[1])
        else:
            res = res + "{} {} {}\n".format(key, store[key][0], store[key][1])

        print(res)
        return res


class ClientServerProtocol(asyncio.Protocol):
    store = dict()

    def connection_made(self, transport):
        try:
            self.transport = transport
            self.parser = Parser()
        except Exception:
            raise ClientSocketError

    def data_received(self, data):
        resp = self.parser.parse(data.decode(), self.store)
        print(self.store)
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server("127.0.0.1", 8888)
