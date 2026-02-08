from pyray import *
from raylib import *

def get_bbox(entity):
    bbox = get_mesh_bounding_box(entity.model.meshes[0])
    min_boundary = Vector3Add(entity.position, bbox.min)
    max_boundary = Vector3Add(entity.position, bbox.max)
    return BoundingBox(min_boundary, max_boundary)


def check_collision(entity, obstacles, axis):
    entity_bbox = get_bbox(entity)    
    for obs in obstacles:        
        obstacle_bbox = get_bbox(obs)
        if check_collision_boxes(entity_bbox, obstacle_bbox):
            if axis == 'x':
                if entity.direction.x > 0:
                    entity.position.x = obstacle_bbox.min.x - 0.25005
                if entity.direction.x < 0:
                    entity.position.x = obstacle_bbox.max.x + 0.25005
            
            if axis == 'z':
                if entity.direction.z > 0:
                    entity.position.z = obstacle_bbox.min.z - 0.25005
                if entity.direction.z < 0:
                    entity.position.z = obstacle_bbox.max.z + 0.25005