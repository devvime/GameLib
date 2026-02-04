from pyray import *
from raylib import *
from os.path import join
from engine.entity import Entity
from engine.animator import Animator

class PlayerSkin(Entity):
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
        self.position = self.scene.player.position
        self.animator.play()
        
        if self.scene.player.is_grounded:
            self.animator.action = 2
        
        if is_key_down(KEY_W) and self.scene.player.is_grounded:
            self.model.transform = matrix_rotate_y(3.1)
            self.animator.action = 6
        
        if is_key_down(KEY_S) and self.scene.player.is_grounded:
            self.model.transform = matrix_rotate_y(0)
            self.animator.action = 6
            
        if is_key_down(KEY_A) and self.scene.player.is_grounded:
            self.model.transform = matrix_rotate_y(-1.6)
            self.animator.action = 6
            
        if is_key_down(KEY_D) and self.scene.player.is_grounded:
            self.model.transform = matrix_rotate_y(1.6)
            self.animator.action = 6
            
        if is_key_pressed(KEY_SPACE):
            self.model.transform = matrix_rotate_y(1.6)
            self.animator.action = 3