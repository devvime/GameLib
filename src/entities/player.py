from pyray import *
from raylib import *
from engine.entity import Entity
from engine.collision import check_collision
from src.entities.player_skin import PlayerSkin

class Player(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model_from_mesh(gen_mesh_cube(0.5, 1, 0.5))
        self.player_skin = PlayerSkin(self.scene)
        self.speed = 5
        self.fall_speed = 2
        self.jump_force = 7
        self.position = Vector3(0,2,0)


    def draw(self):
        draw_model_wires(self.model, self.position, 1, RED)
        self.player_skin.draw()
        
    def update(self, dt):        
        self.movement(dt)        
        self.jump()
        self.player_skin.update(dt)


    def movement(self, dt):
        self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        self.direction.z = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        
        self.position.x += self.direction.x * dt * self.speed
        check_collision(self, self.scene.objects3d, 'x')
        self.position.z += self.direction.z * dt * self.speed
        check_collision(self, self.scene.objects3d, 'z')


    def jump(self):
        if self.is_grounded and is_key_down(KEY_SPACE):
            self.velocity.y += self.jump_force
