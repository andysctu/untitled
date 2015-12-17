import pyglet 
import physicalobject
from pyglet.window import key

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')



seth = physicalobject.PhysicalObject()
game_objects = [seth]

def update(dt):
	for obj in game_objects:
		obj.update(dt)

window.push_handlers(pyglet.window.event.WindowEventLogger())
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
