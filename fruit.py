import numpy as np

class Fruit:
    def __init__(self, _game_area) -> None:
        print("fruit: spawn")
        self.game_area = _game_area
        self.position = (np.rand(self.game_area.min_x, self.game_area.max_x), np.rand(self.game_area.min_y, self.game_area.max_y))
    
    def __del__(self):
        print("fruit: eaten")