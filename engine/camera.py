from raylib import *
from pyray import *
from src.settings import * 

camera = Camera3D()
camera.position = Vector3(0,7, 10)
camera.up = Vector3(0, 1, 0)
camera.fovy = 60
camera.projection = CAMERA_PERSPECTIVE