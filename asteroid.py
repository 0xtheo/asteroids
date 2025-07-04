from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (128, 128, 128), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt 

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        pos_vector = self.velocity.rotate(random_angle)
        neg_vector = self.velocity.rotate(random_angle * -1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        pos_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        neg_asteroid = Asteroid(self.position.x, self.position.y, new_radius)

        pos_asteroid.velocity = pos_vector * 1.2
        neg_asteroid.velocity = neg_vector * 1.2