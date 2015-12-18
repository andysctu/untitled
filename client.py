import asyncio
import pyglet
import json
from constants import ADDR, RENDER_WAIT

LOOP = asyncio.get_event_loop()
DATA_RECEIVED = None
TRANSPORT = None


def run_pyglet():
    pyglet.clock.tick()
    for window in pyglet.app.windows:
        window.switch_to()
        window.dispatch_events()
        window.dispatch_event('on_draw')
        window.flip()
    LOOP.call_later(RENDER_WAIT, run_pyglet)


class EchoClient(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        print('connection made')
        global TRANSPORT
        TRANSPORT = transport
        run_pyglet()

    def datagram_received(self, data, addr):
        DATA_RECEIVED(json.loads(data.decode()))

    def connection_lost(self, exc):
        print('server closed the connection')
        LOOP.stop()


def start_client(data_received_callback=None):
    global DATA_RECEIVED
    DATA_RECEIVED = data_received_callback
    coro = LOOP.create_datagram_endpoint(EchoClient, remote_addr=ADDR)
    LOOP.run_until_complete(coro)
    try:
        LOOP.run_forever()
        ##blocked
    except KeyboardInterrupt:
        print('exit')
    finally:
        LOOP.close()
