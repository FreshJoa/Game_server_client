import pygame
from network import Network
import pickle
from grid import Grid
from player import  Player

pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
grid=Grid(width, height)

class Interactive_text:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    # def click(self, pos):
    #     x1 = pos[0]
    #     y1 = pos[1]
    #     if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
    #         return True
    #     else:
    #         return False


def redrawWindow(win, game, p):
    win.fill((128,128,128))

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 80)
        text = font.render("Waiting for Player...", 1, (255,0,0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 60)


        grid.draw_grid(win)

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = font.render(move1, 1, (0,0,0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if not game.p1Went and p == 0:
                text1=font.render("Your Move", 1, (0, 255,255))
            elif game.p1Went and p == 0:
                text1 = font.render(move1, 1, (0,0,0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if not game.p2Went and p == 1:
                text2 = font.render("Your Move", 1, (0, 255, 255))
            elif game.p1Went and p == 1:
                text2 = font.render(move2, 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))
        if p == 1:
            win.blit(text1, (width/2 - text1.get_width()/2, height/2 - text1.get_height()/2))
        else:
            win.blit(text2, (width/2 - text2.get_width()/2, height/2 - text2.get_height()/2))

        # for btn in btns:
        #     btn.draw(win)

    pygame.display.update()




#btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]
def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = Player(int(n.getP()))
    player.set_symbol()
    print("You are player  ", player.get_symbol())

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            redrawWindow(win, game, player.get_number())
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            # font = pygame.font.SysFont("comicsans", 90)
            # if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
            #     text = font.render("You Won!", 1, (255,0,0))
            # elif game.winner() == -1:
            #     text = font.render("Tie Game!", 1, (255,0,0))
            # else:
            #     text = font.render("You Lost...", 1, (255, 0, 0))
            #
            # win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            # pygame.display.update()
            # pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
                # pos = pygame.mouse.get_pos()
                # for btn in btns:
                #     if btn.click(pos) and game.connected():
                #         if player == 0:
                #             if not game.p1Went:
                #                 n.send(btn.text)
                #         else:
                #             if not game.p2Went:
                #                 n.send(btn.text)

        redrawWindow(win, game, player.get_number())

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()