import pyray as rl
from os.path import join

rl.init_window(800, 600, "GLB Animation - Raylib Python")
rl.set_target_fps(60)

camera = rl.Camera3D()
camera.position = rl.Vector3(6, 6, 6)
camera.up = rl.Vector3(0, 1, 0)
camera.fovy = 60 
camera.projection = rl.CAMERA_PERSPECTIVE

# Carrega o modelo
model = rl.load_model(join("assets","models","robot.glb"))

# Carrega as animações
anim_count = rl.ffi.new("int *")
anims = rl.load_model_animations(join("assets","models","robot.glb"), anim_count)
print(anims)

current_anim = 0
frame = 0

while not rl.window_should_close():

    # Avança a animação
    frame += 1
    if frame >= anims[current_anim].frameCount:
        frame = 0
        
    rl.update_model_animation(
        model,
        anims[current_anim],
        frame
    )
    
    # rl.update_camera(camera, rl.CAMERA_FREE)

    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)

    rl.begin_mode_3d(camera)
    
    rl.draw_model(model, rl.Vector3(0, 0, 0), 1.0, rl.WHITE)
    rl.draw_grid(10, 1)
    
    rl.end_mode_3d()

    rl.draw_text(f"Frames: {anims[current_anim].frameCount}", 10, 10, 20, rl.BLACK)

    rl.end_drawing()

# Limpeza
rl.unload_model(model)
for i in range(anim_count[0]):
    rl.unload_model_animation(anims[i])

rl.close_window()