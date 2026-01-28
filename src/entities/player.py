from pyray import *
from raylib import *
from engine.entity import Entity
from engine.collision import check_collision

class Player(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
        self.speed = 5
        self.fall_speed = 2
        self.jump_force = 7
        self.position = Vector3(0,2,0)
        
    def draw(self):
        draw_model(self.model, self.position, 1, RED)
        
    def update(self, dt):        
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction.z = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        
        self.position.x += self.direction.x * dt * self.speed
        check_collision(self, self.scene.objects3d, 'x')
        self.position.z += self.direction.z * dt * self.speed
        check_collision(self, self.scene.objects3d, 'z')
        
        self.jump()
        
    def jump(self):
        if self.is_grounded and is_key_down(KEY_SPACE):
            self.velocity.y += self.jump_force
