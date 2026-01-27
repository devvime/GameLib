from pyray import *
from raylib import *
from engine.collision import get_bbox
from src.settings import GRAVITY

def set_gravity(entity, obstacles, dt):
    entity.velocity.y -= GRAVITY * dt * entity.fall_speed
    entity.position.y += entity.velocity.y * dt
    
    for obstacle in obstacles:        
        if check_collision_boxes(get_bbox(entity), get_bbox(obstacle)):            
            if entity.position.y > get_bbox(obstacle).max.y:
                entity.position.y = get_bbox(obstacle).max.y + 0.5001
                
            entity.velocity.y = 0
            entity.is_grounded = True
        
    entity.is_grounded = False    
    if entity.velocity.y == 0:
        entity.is_grounded = True