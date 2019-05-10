import pygame
from network import Network
from player import Player


width = 700
height = 700

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawwindowdow(window, player, player2):
    window.fill((255, 255, 100))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    n=Network()
    p=n.getP()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawwindowdow(window, p, p2)


main()
