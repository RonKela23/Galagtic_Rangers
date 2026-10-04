from asteroid import Asteroid
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from logger import log_event
import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field1 = AsteroidField()
    player1 = Player(x = SCREEN_WIDTH /2, y = SCREEN_HEIGHT /2)



    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player1) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for s in shots:
                if asteroid.collides_with(s) == True:
                    s.kill()
                    log_event("asteroid_shot")
                    asteroid.split()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()





if __name__ == "__main__":
    main()
