class Scene:
    def __init__(self, game):
        self.game = game
        self.objects2d = []
        self.objects3d = []
        
    def create(self):
        ...
        
    def draw_2d(self):
        for obj in self.objects2d:
            obj.draw()
        
    def draw_3d(self):
        for obj in self.objects3d:
            obj.draw()
        
    def update(self, dt):
        ...