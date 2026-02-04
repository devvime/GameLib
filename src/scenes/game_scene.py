from src.settings import *
from engine.scene import Scene
from engine.gravity import set_gravity
from src.entities.player import Player
from src.entities.obstacle import Obstacle
from src.entities.player_test import PlayerTest

class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        
    def create(self):
        super().create()
        
        self.player = Player(self)
        self.player_test = PlayerTest(self)
        self.objects3d = [
            Obstacle(self, position=Vector3(3, 1.5, 0), scale=Vector3(2, 1, 4), color=DARKGRAY),
            Obstacle(self, position=Vector3(0, 0.5, 0), scale=Vector3(10, 1, 10)),
            Obstacle(self, position=Vector3(9, 0.5, 0), scale=Vector3(5, 1, 5))
        ]
    
    def draw_2d(self):
        super().draw_2d()
    
    def draw_3d(self):
        super().draw_3d()
        
        draw_grid(10, 0.5)
        self.player.draw()
        self.player_test.draw()
    
    def update(self, dt):
        super().update(dt)
        
        set_gravity(self.player, self.objects3d, dt)
        
        if is_key_pressed(KEY_ESCAPE):
            self.game.set_scene("main")
            
        self.player.update(dt)
        self.player_test.update(dt)