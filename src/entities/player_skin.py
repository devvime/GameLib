from pyray import *
from raylib import *
from os.path import join
from engine.entity import Entity
from engine.animator import Animator

class PlayerSkin(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model(join("assets", "models", "robot.glb"))
        self.position = Vector3(0, 1, 0)
        self.animator = Animator(self.model, join("assets", "models", "robot.glb"))        
        self.animator.change_action(2)
        self.rotate_y = 0


    def draw(self):
        draw_model(self.model, self.position, 0.3, WHITE)
        
        
    def animate(self, dt):
        self.animator.play()
        
        if self.scene.player.is_grounded:
            self.animator.action = 2
            self.model.transform = matrix_rotate_y(self.rotate_y)

            if is_key_down(KEY_W) and is_key_down(KEY_D):
                self.rotate_y = 2.3
                self.animator.action = 6                
            elif is_key_down(KEY_W) and is_key_down(KEY_A):
                self.rotate_y = -2.3
                self.animator.action = 6
            elif is_key_down(KEY_S) and is_key_down(KEY_D):
                self.rotate_y = 1.15
                self.animator.action = 6
            elif is_key_down(KEY_S) and is_key_down(KEY_A):
                self.rotate_y = -1.15
                self.animator.action = 6
            
            elif is_key_down(KEY_W):
                self.rotate_y = 3.1
                self.animator.action = 6            
            elif is_key_down(KEY_S):
                self.rotate_y = 0
                self.animator.action = 6                
            elif is_key_down(KEY_A):
                self.rotate_y = -1.6
                self.animator.action = 6                
            elif is_key_down(KEY_D):
                self.rotate_y = 1.6
                self.animator.action = 6                
            if is_key_pressed(KEY_SPACE):
                self.animator.action = 3


    def update(self, dt):
        self.position = self.scene.player.position
        self.animate(dt)