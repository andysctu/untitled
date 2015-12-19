import pyglet 
import physicalobject
import assets
from pyglet.window import key

window = pyglet.window.Window()
toggle = True
@window.event
def on_draw():
    window.clear()
    if toggle:
    	seth.draw()
    else:
    	seth2.draw()
    toggle = not toggle

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

seth = pyglet.sprite.Sprite(img=assets.player_image, x=400, y=300)
seth2 = pyglet.sprite.Sprite(img=assets.player_image2, x=400, y=300)



# seth = physicalobject.PhysicalObject()
# game_objects = [seth]

# def update(dt):
# 	for obj in game_objects:
# 		obj.update(dt)

# window.push_handlers(pyglet.window.event.WindowEventLogger())
# pyglet.clock.schedule_interval(update, 1/120.0)


if __name__ == '__main__':
	pyglet.app.run()
