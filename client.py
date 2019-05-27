#!/home/mazurek/anaconda3/bin/python
import pygame
from network import Network
from player import Player


pygame.font.init()
#create the window
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

#function which redraw winodow after each move and also give information who is winner or about tie
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
    elif player.finish() or player2.finish():
        text = font.render("Nobody is winner", 1, (0, 255, 255))
        window.blit(text, (80, 200))

    pygame.display.update()



def main():
    run = True
    n=Network()
    #when it will be first connect to server it return each of the clients the starting positione ()
    p=n.getP()
    #print("p=n.getP() ", p)

    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Waiting for Player...", 1, (255, 0, 0), True)
    window.blit(text, (width / 2 - text.get_width() / 2, height / 2 - text.get_height() / 2))


    pygame.display.update()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        #send all current position of players
        p2 = n.send(p)
        #print("n.send(p) ", p2)
        redrawwindowdow(window, p, p2)


        #if we wnat to close window it closes the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        #if we press mousebutton it gets position and update window
        if event.type == pygame.MOUSEBUTTONDOWN:
            #time.sleep(0.5)
            pos = pygame.mouse.get_pos()
            #it is condition that we can't press the mouse on posotion where is some symbol
            if not p.get_cell_value(pos[0] // 200, pos[1] // 200) and not p2.get_cell_value(pos[0] // 200, pos[1] // 200):
                p.move(pos)
           


        #update the window
        redrawwindowdow(window, p, p2)


main()
