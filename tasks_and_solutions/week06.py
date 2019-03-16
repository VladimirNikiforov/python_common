import asyncio

d = {}
order = []


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def process_data(self, data):
        if data.startswith('put'):
            try:
                _, key, r, l = data.split(' ')
                if key in d:
                    ll = len(d[key])
                    l_founded = False
                    for x in range(ll):
                        if int(l) == d[key][x][0]:
                            d[key][x] = (int(l), float(r))
                            l_founded = True
                            break
                    if not l_founded:
                        d[key].append((int(l), float(r)))
                else:
                    d[key] = [(int(l), float(r))]
                    order.append(key)
                return "ok\n\n"
            except Exception as e:
                return "error\n"+e+"\n\n"
        elif data.startswith('get'):
            try:
                _, key = data.rstrip('\n').split(' ')
                if key == "*":
                    # return all keys
                    l = "ok\n"
                    for o in order:
                        for x in d[o]:
                            l += o + " " + str(x[1]) + " " + str(int(x[0])) + "\n"
                    return l + "\n"
                else:
                    if key in d:
                        l = "ok\n"
                        for x in d[key]:
                            l += key + " " + str(x[1]) + " " + str(int(x[0])) + " " + "\n"
                        return l + "\n"
                    else:
                        return "{}\n\n"
            except Exception as e:
                return "error\n"+e+"\n\n"
        else:
            return "error\nwrong command\n\n"

    def data_received(self, data):
        resp = self.process_data(data.decode())
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

if __name__ == "__main__":
    run_server("127.0.0.1", 8888)