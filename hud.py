import pygame

class HUD :
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def update_score(self, _score):
        self.score = self.font.render("Score: " + str(_score), True, (255, 255, 255))

    def draw(self, _surface):
        _surface.blit(self.score, (10, 10))