import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):        
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        split_angle = random.uniform(20, 50)
        new_rotation1 = self.velocity.rotate(split_angle)
        new_rotation2 = self.velocity.rotate(-split_angle)
        child_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_asteroid1.velocity = new_rotation1 * 1.2
        child_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        child_asteroid2.velocity = new_rotation2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)