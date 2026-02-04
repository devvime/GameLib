from pyray import *
from raylib import *
from os.path import join
from engine.entity import Entity
from engine.animator import Animator

class PlayerTest(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model(join("assets", "models", "robot.glb"))
        self.model.transform = matrix_rotate_y(3.1)
        self.position = Vector3(0, 1, 0)
        self.animator = Animator(self.model, join("assets", "models", "robot.glb"))
        
        self.animator.change_action(2)


    def draw(self):
        draw_model(self.model, self.position, 0.5, WHITE)


    def update(self, dt):
        self.animator.play()
        
        if is_key_pressed(KEY_W):
            self.animator.change_action(6)