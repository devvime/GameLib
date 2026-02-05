from pyray import *
from raylib import *
from engine.camera import camera

def lerp(a, b, t):
    return a + (b - a) * t


def lerp_vec3(a: Vector3, b: Vector3, t: float):
    return Vector3(
        lerp(a.x, b.x, t),
        lerp(a.y, b.y, t),
        lerp(a.z, b.z, t),
    )


def CameraFollow(player, camera_offset = Vector3(0, 10, 7), camera_smooth = 0.05):
    desired_pos = Vector3Add(player.position, camera_offset)

    camera.position = lerp_vec3(
        camera.position,
        desired_pos,
        camera_smooth
    )

    camera.target = lerp_vec3(
        camera.target,
        player.position,
        camera_smooth
    )