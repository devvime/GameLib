from src.scenes.main_scene import MainScene
from src.scenes.game_scene import GameScene

def init_scenes(game):
    game.scenes = {
        "main": MainScene(game),
        "game": GameScene(game)
    }