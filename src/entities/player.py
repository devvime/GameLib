from pyray import *
from raylib import *
from engine.entity import Entity
from engine.collision import check_collision
import math

class Player(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model_from_mesh(gen_mesh_cube(1, 1, 1))
        self.speed = 5
        self.fall_speed = 2
        self.jump_force = 7
        self.position = Vector3(0,2,0)
        
        self.rotation_y = 0.0
        self.turn_speed = 160


    def draw(self):
        # draw_model(self.model, self.position, 1, RED)
        draw_model_ex(
            self.scene.player_skin.model,
            self.position,
            Vector3(0, 1, 0),  # eixo Y
            self.rotation_y,
            Vector3(0.3, 0.3, 0.3),
            WHITE
        )
        
    def update(self, dt):        
        self.movement(dt)        
        self.jump()


    def movement(self, dt):
        # self.direction.x = int(is_key_down(KEY_D)) - int(is_key_down(KEY_A))
        # self.direction.z = int(is_key_down(KEY_S)) - int(is_key_down(KEY_W))
        
        # self.position.x += self.direction.x * dt * self.speed
        # check_collision(self, self.scene.objects3d, 'x')
        # self.position.z += self.direction.z * dt * self.speed
        # check_collision(self, self.scene.objects3d, 'z')
        
        if is_key_down(KEY_A):
            self.rotation_y += self.turn_speed * dt
        if is_key_down(KEY_D):
            self.rotation_y -= self.turn_speed * dt
            
        rad = math.radians(self.rotation_y)
        forward = Vector3(
            math.sin(rad),
            0,
            math.cos(rad)
        )

        move = 0
        if is_key_down(KEY_W):
            move += 1
        if is_key_down(KEY_S):
            move -= 1
            
        move_vec = Vector3(
            forward.x * move * self.speed * dt,
            0,
            forward.z * move * self.speed * dt
        )

        self.position.x += forward.x * move * self.speed * dt
        check_collision(self, self.scene.objects3d, move_vec)

        self.position.z += forward.z * move * self.speed * dt
        check_collision(self, self.scene.objects3d, move_vec)


    def jump(self):
        if self.is_grounded and is_key_down(KEY_SPACE):
            self.velocity.y += self.jump_force
