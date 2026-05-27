import pygame 
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
import asteroids
from asteroids import Asteroid
from asteroids import AsteroidField 
from logger import log_event   
import sys 


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt=0.0 
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        screen.fill('black')

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for obj in drawable:
            obj.draw(screen)

        

        pygame.display.flip()
       
        dt=clock.tick(60)/1000.0
        

    

if __name__ == "__main__":
    main()
