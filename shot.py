import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED, LINE_WIDTH

class Shot(CircleShape):
    containers = ()   

    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)

        #Direction the shot travels
        direction = pygame.Vector2(0, 1).rotate(rotation)

        #Velocity is direction * speed
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        #Move the shot
        self.position += self.velocity * dt

        #Remove if off-screen
        if (
            self.position.x < 0 or self.position.x > 800 or
            self.position.y < 0 or self.position.y > 600
        ):
            self.kill()
