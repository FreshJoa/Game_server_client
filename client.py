import pygame
from network import Network


width = 700
height = 700

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.widtth = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 3

    def draw(self, window):
        pygame.draw.rect(window , self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()  # get the state of all keyboard buttons

        if keys[pygame.K_LEFT]:
            self.x -= self.val

        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.widtth, self.height)

def read_pos(str):
    str=str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawwindowdow(window, player, player2):
    window.fill((255, 255, 100))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    n=Network()
    startPos=read_pos(n.getPos())
    p = Player(startPos[0],startPos[1], 100, 100, (33, 250, 230))
    p2 = Player(0, 0, 100, 100, (33, 250, 230))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2Pos=read_pos(n.send(make_pos((p.x, p.y))))
        p2.x=p2Pos[0]
        p2.y=p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawwindowdow(window, p, p2)


main()
