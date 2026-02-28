import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    
    #1 Create groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #2 Register Player class with groups

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Register asteroid and asteroidfield; instantiate asteroidfield

    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    field = AsteroidField()

    #3 Create the player

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0

    font = pygame.font.Font(None, 36)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        dt = clock.tick(60) / 1000

        #4 Use groups

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()
                    log_event("asteroid_shot")
                    score += 10

        log_state()

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))

        pygame.display.flip()

if __name__ == "__main__":
    main()
