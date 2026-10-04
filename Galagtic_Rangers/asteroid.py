import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame





from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt: float) -> None:
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angel = random.uniform(20,50)
            asteroid1_angel = self.velocity.rotate(new_angel)
            asteroid2_angel = self.velocity.rotate(new_angel * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 =Asteroid(self.position.x, self.position.y, new_radius)

            new_asteroid1.velocity = asteroid1_angel * 1.2
            new_asteroid2.velocity = asteroid2_angel * 1.2
