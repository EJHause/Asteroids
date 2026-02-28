import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    
    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill() #kill the original asteroid

        # if too small, no splitting
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # log the split event
        log_event("asteroid_split")

        # random angle between 20 and 50 degrees
        angle = random.uniform(20, 50)

        # Create two new velocity vectors
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #create 2 new asteroids
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)

        a1.velocity = vel1
        a2.velocity = vel2

    def bounce(self, normal):
        self.velocity = self.velocity.reflect(normal)

