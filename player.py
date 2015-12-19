import json
import uuid
import pyglet
import physicalobject


class Player(physicalobjet.PhysicalObject):
    def __init__(self, id=None, name=None, batch=None):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.hp = 10
        
        # For server only
        self.key_state = {"UP": False, "DOWN": False,
                          "LEFT": False, "RIGHT": False}
        self.prev_key_state = {"UP": False, "DOWN": False,
                               "LEFT": False, "RIGHT": False}

    # TODO: Let's migrate to using something like this. It's not yet fully
    #       fleshed out as an idea yet, but it should allow us to use the same
    #       class on both the server and the client.
    def get_datagram(self) -> bytes:
        """Every get_datagram method on a class is used to get the bytes to
        send across the wire.
        """
        return json.dumps({
            "type": "player",
            "id": self.id,
            "name": self.name,
            "position": list(self.body.position),
            "direction": self.direction,
            "movement": self.movement,
            "hp": self.hp,
        }).encode()

    def read_datagram(self, data) -> None:
        """Every read_datagram method on a class is used to get the datagram's
        data back into the object.
        """
        self.hp = data["hp"]
        self.body.position = Vec2d(data["position"])
        self.direction = data["direction"]
        self.movement = data["movement"]
        self.update()
