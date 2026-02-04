from pyray import *
from raylib import *
from os.path import join

class Animator:
    def __init__(self, model, anims):
        self.anim_count = ffi.new("int *")
        self.model = model
        self.anims = load_model_animations(anims, self.anim_count)
        self.frame = 0
        self.action = 0
        
    
    def change_action(self, action: int):
        self.frame = 0
        self.action = action


    def play(self):
        self.frame += 1
        if self.frame >= self.anims[self.action].frameCount:
            self.frame = 0
            
        update_model_animation(
            self.model,
            self.anims[self.action],
            self.frame
        )


    def destroy(self):
        for i in range(self.anim_count[0]):
            unload_model_animation(self.anims[i])