from pyray import *
from raylib import *
from engine.entity import Entity
from engine.collision import check_collision
from engine.gravity import set_gravity

class Player(Entity):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene
        self.model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
        self.speed = 5
        self.fall_speed = 2
        self.jump_force = 7
        
    def draw(self):
        draw_model(self.model, self.position, 1, RED)
        
    def update(self, dt):
        set_gravity(self, [self.scene.ground], dt)
        
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction.z = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        
        self.position.x += self.direction.x * dt * self.speed
        check_collision(self, self.scene.obstacle, 'x')
        self.position.z += self.direction.z * dt * self.speed
        check_collision(self, self.scene.obstacle, 'z')
        
        self.jump()
        
    def jump(self):
        if self.is_grounded and is_key_down(KEY_SPACE):
            self.velocity.y += self.jump_force