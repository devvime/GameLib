from src.settings import *
from src.entities.ship import Ship
from src.entities.player import Player
from src.entities.obstacle import Obstacle

class GameScene:
    def __init__(self, game):
        self.game = game
        
    def create(self):
        # self.ship = Ship()
        self.player = Player(self)
        self.obstacle = Obstacle(position=Vector3(3, 0, 0), scale=Vector3(2, 1, 4), color=DARKGRAY)
        self.ground = Obstacle(position=Vector3(0, -1, 0), scale=Vector3(10, 1, 10))
    
    def draw_2d(self):
        ...
    
    def draw_3d(self):
        draw_grid(10, 0.5)
        # self.ship.draw()
        self.player.draw()
        self.obstacle.draw()
        self.ground.draw()
    
    def update(self, dt):
        if is_key_pressed(KEY_ESCAPE):
            self.game.set_scene("main")
            
        # self.ship.update(dt)
        self.player.update(dt)
        self.obstacle.update(dt)
        self.obstacle.update(dt)