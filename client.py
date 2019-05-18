import pygame
from network import Network
from player import Player


width = 600
height = 600

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
    print("p=n.getP() ", p)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        print("n.send(p) ", p2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            p.move(pos)

        redrawwindowdow(window, p, p2)


main()