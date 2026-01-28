from src.settings import *
from engine.scene import Scene
from engine.gravity import set_gravity
from src.entities.ship import Ship
from src.entities.player import Player
from src.entities.obstacle import Obstacle

class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        
    def create(self):
        self.ship = Ship(self)
        self.player = Player(self)
        self.objects3d = [
            Obstacle(self, position=Vector3(3, 2, 0), scale=Vector3(2, 1, 4), color=DARKGRAY),
            Obstacle(self, position=Vector3(0, 1, 0), scale=Vector3(10, 1, 10)),
            Obstacle(self, position=Vector3(9, 1, 0), scale=Vector3(5, 1, 5)),
            self.ship
        ]
    
    def draw_2d(self):
        ...
    
    def draw_3d(self):
        draw_grid(10, 0.5)
        self.ship.draw()
        self.player.draw()
        
        for ob in self.objects3d:
            ob.draw()
    
    def update(self, dt):
        set_gravity(self.player, self.objects3d, dt)
        
        if is_key_pressed(KEY_ESCAPE):
            self.game.set_scene("main")
            
        # self.ship.update(dt)
        self.player.update(dt)