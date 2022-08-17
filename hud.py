import pygame

class HUD :
    def __init__(self, _width, _height):
        self.width = _width
        self.heigh = _height
        self.font = pygame.font.Font(None, 36)

    def update_score(self, _score):
        self.score = self.font.render("Score: " + str(_score), True, (255, 255, 255))

    def update_time(self, _seconds, _minutes):
        self.time = self.font.render(str(_minutes)+":"+str(_seconds), True, (255, 255, 255))

    def draw(self, _surface):
        _surface.blit(self.score, (10, 10))
        _surface.blit(self.time, (self.width - self.time.get_width(), 10))