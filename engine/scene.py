class Scene:
    def __init__(self, game):
        self.game = game
        self.objects2d = []
        self.objects3d = []
        
    def create(self):
        ...
        
    def draw_2d(self):
        for ob in self.objects2d:
            ob.draw()
        
    def draw_3d(self):
        for ob in self.objects3d:
            ob.draw()
        
    def update(self, dt):
        ...