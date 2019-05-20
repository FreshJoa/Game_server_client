import pygame
from network import Network
from player import Player


pygame.font.init()
width = 600
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawwindowdow(window, player, player2):
    window.fill((255, 255, 100))
    player.draw(window)
    player2.draw(window)
    font = pygame.font.SysFont("comicsans", 60)


    if player.winner():
        text = font.render("Player " +player.symbol+" is winner", 1, (0, 255, 255))
        window.blit(text, (80, 200))
    elif player2.winner():
        text = font.render("Player "+player2.symbol+" is winner", 1, (0, 255, 255))
        window.blit(text, (80, 200))
    elif player.finish():
        text = font.render("Nobody is winner", 1, (0, 255, 255))
        window.blit(text, (80, 200))

    pygame.display.update()



def main():
    run = True
    n=Network()
    p=n.getP()
    #print("p=n.getP() ", p)

    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
    window.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))


    pygame.display.update()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        #print("n.send(p) ", p2)
        redrawwindowdow(window, p, p2)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #time.sleep(0.5)
            pos = pygame.mouse.get_pos()
            if not p.get_cell_value(pos[0] // 200, pos[1] // 200) and not p2.get_cell_value(pos[0] // 200, pos[1] // 200):
                p.move(pos)
            #     can=True
            # elif p.get_cell_value(pos[0] // 200, pos[1] // 200) or p2.get_cell_value(pos[0] // 200, pos[1] // 200):
            #     can=False




        redrawwindowdow(window, p, p2)


main()