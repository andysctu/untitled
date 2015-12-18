import pyglet
from pyglet.window import key
import asyncio
import random
import json
from client import start_client
from constants import ADDR, NETWORK_WAIT

NAME = ''.join(str(chr(random.randint(97, 122))) for i in range(0, random.randint(3, 12)))
print(NAME)

window = pyglet.window.Window()

PLAYERS = {}
KEY_STATES = { 'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'NAME': NAME }

LOOP = asyncio.get_event_loop()


def send_data():
    from client import TRANSPORT
    if TRANSPORT:
        TRANSPORT.sendto(json.dumps(KEY_STATES).encode(), ADDR)
    LOOP.call_later(NETWORK_WAIT, send_data)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        KEY_STATES['UP'] = True
    elif symbol == key.DOWN:
        KEY_STATES['DOWN'] = True
    elif symbol == key.LEFT:
        KEY_STATES['LEFT'] = True
    elif symbol == key.RIGHT:
        KEY_STATES['RIGHT'] = True


@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        KEY_STATES['UP'] = False
    elif symbol == key.DOWN:
        KEY_STATES['DOWN'] = False
    elif symbol == key.LEFT:
        KEY_STATES['LEFT'] = False
    elif symbol == key.RIGHT:
        KEY_STATES['RIGHT'] = False


def data_received(data):
    name = data['NAME']
    if name not in PLAYERS.keys():
        print('player {} added'.format(name))
    if PLAYERS.get(name) != data:
        print(data)
    PLAYERS[name] = data


LOOP.call_later(NETWORK_WAIT, send_data)
start_client(data_received_callback=data_received)
