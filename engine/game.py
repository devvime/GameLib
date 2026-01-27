from src.settings import * 
import asyncio

from src.init_scenes import init_scenes
from engine.camera import camera

class Game:
    def __init__(self):        
        init_window(WIDTH, HEIGHT, GAME_TITLE)
        set_exit_key(0)
        set_target_fps(60)
        init_audio_device()        
        init_scenes(self)        
        self.set_scene("main")
        self.paused = False
        
    def pause(self):
        self.paused = True
        
    def resume(self):
        self.paused = False
        
    def set_scene(self, scene):
        self.current_scene = self.scenes[scene]
        self.current_scene.create()
        
    def update(self):
        if not self.paused:            
            dt = get_frame_time()
            self.current_scene.update(dt)
        
    def draw(self):
        clear_background(BG_COLOR)        
        begin_drawing()
        if DEBUG: draw_fps(10, 10)
        self.current_scene.draw_2d()
        begin_mode_3d(camera)
        self.current_scene.draw_3d()
        end_mode_3d()
        end_drawing()
        
    async def run(self):
        while not window_should_close():
            if is_key_pressed(KEY_F11):
                toggle_fullscreen()
            if not self.paused:    
                self.update()
                self.draw()
            await asyncio.sleep(0) 
        close_audio_device()
        close_window()
        
    def close():
        close_audio_device()
        close_window()