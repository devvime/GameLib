from pyray import *
from raylib import *

class Entity:
    def __init__(self):
        self.model = None
        self.position = Vector3()
        self.direction = Vector3()
        self.velocity = Vector3()
        self.is_grounded = False