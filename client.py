
import pygame
import colored

width=700
height=700

win=pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")

clientNumber=0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x=x
        self.y=y
        self.widtth=width
        self.height=height
        self.color=color
        self.rect=(x, y, width, height)
        self.val=3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys= pygame.key.get_pressed() #get the state of all keyboard buttons

        if keys[pygame.K_LEFT]:
            self.x -=self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.rect=(self.x , self.y, self.widtth, self.height )

def redrawWindow(win,player):
    win.fill((255,255,100))
    player.draw(win)
    pygame.display.update()


def main():
    run=True
    p=Player(50, 50, 100, 100, (33, 250, 230))
    clock=pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()
        p.move()
        redrawWindow(win, p)
main()