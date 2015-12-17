import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
	'All PhysicalObjects are subjet to gravity and collisions with other PhysicalObjects'
	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args, **kwargs)
		self.velocity_x = 0.0
		self.velocity_y = 0.0
	def update(dt):
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt