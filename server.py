import asyncio
import json
from constants import ADDR, NETWORK_WAIT

LOOP = asyncio.get_event_loop()
CLIENTS = {}
TRANSPORT = None


class EchoServer(asyncio.DatagramProtocol):
    def datagram_received(self, data, addr):
        blob = json.loads(data.decode())
        CLIENTS[addr] = blob

    def error_received(self, exc):
        print(exc)


def broadcast(encoded):
    for c in CLIENTS.keys():
        TRANSPORT.sendto(encoded, c)


def send_game_state():
    for player in CLIENTS.values():
        broadcast(json.dumps(player).encode())


def update():
    return


def check_step():
    update()
    send_game_state()
    LOOP.call_later(NETWORK_WAIT, callback=check_step)


print('starting server on ' + str(ADDR))
coro = LOOP.create_datagram_endpoint(EchoServer, local_addr=ADDR)
TRANSPORT, server = LOOP.run_until_complete(coro)
LOOP.call_later(NETWORK_WAIT, check_step)

try:
    LOOP.run_forever()
    ##blocked
except KeyboardInterrupt:
    print('exit')
finally:
    TRANSPORT.close()
    LOOP.close()
