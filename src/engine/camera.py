from src.settings import * 

camera = Camera3D()
camera.position = Vector3(-4.0, 8.0, 6.0) 
camera.target = Vector3(0.0, 0.0, -1.0) 
camera.up = Vector3(0.0, 1.0, 0.0) 
camera.fovy = 45.0 
camera.projection = CAMERA_PERSPECTIVE