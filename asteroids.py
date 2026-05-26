
from circleshape import CircleShape
from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position.center(), self.radius, 2)