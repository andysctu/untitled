import pyglet

pyglet.resource.path = ['./assets']
pyglet.resource.reindex()

player_image = pyglet.resource.image('pikachu1.png')
player_image2 = pyglet.resource.image('pikachu2.png')


def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(player_image)