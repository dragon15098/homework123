from player import Player
import pygame
from box import Box
from gate import Gate

class Map:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.player = Player(1, 1)
        self.box = Box(2, 2)
        self.gate = Gate(3,3)

    def in_map(self, x, y, screen_width, screen_height):
        if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
            return False
        return True

    def win(self, bx, by, gx, gy):
        if (bx == gx) and (by == gy):
            return True
        return False

    def move_player(self, dx, dy):
        self.player.nextx = self.player.x + dx
        self.player.nexty = self.player.y + dy
        self.box.nextx = self.box.x + dx
        self.box.nexty = self.box.y + dy
        if (self.in_map(self.player.nextx, self.player.nexty, self.weight, self.height)):
            if self.box.check_match(self.player.nextx, self.player.nexty) and self.in_map(self.box.nextx,
                                                                                          self.box.nexty, self.weight,
                                                                                          self.height):
                self.box.x = self.box.nextx
                self.box.y = self.box.nexty
                self.player.x = self.player.nextx
                self.player.y = self.player.nexty
            elif not self.box.check_match(self.player.nextx, self.player.nexty):
                self.player.x = self.player.nextx
                self.player.y = self.player.nexty

    def print_map(self):
        pygame.init()
        screen = pygame.display.set_mode([800, 600])
        done = False

        # draw bg
        COLOR_WHITE = (255, 255, 255)

        # draw image
        p_image = pygame.image.load("mario.png")
        bg_image = pygame.image.load("square.png")
        box_image = pygame.image.load("box.jpg")
        win_image = pygame.image.load("win.jpg")
        gate_image = pygame.image.load("gate.jpg")
        SQUARE_SIZE = 32

        while not done:
            # get event
            dx, dy = 0, 0
            # process game events
            # repaint
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    if event.key == pygame.K_RIGHT:
                        dx = 1
                    if event.key == pygame.K_UP:
                        dy = -1
                    if event.key == pygame.K_DOWN:
                        dy = 1
                if (dx != 1) or (dy != 1):
                    self.move_player(dx, dy)

            screen.fill(COLOR_WHITE)
            screen.blit(p_image, (self.player.x * SQUARE_SIZE, self.player.y * SQUARE_SIZE))
            screen.blit(box_image, (self.box.x * SQUARE_SIZE, self.box.y * SQUARE_SIZE))
            screen.blit(gate_image,(self.gate.x * SQUARE_SIZE, self.gate.y * SQUARE_SIZE))
            for y in range(self.height):
                for x in range(self.weight):
                    screen.blit(bg_image, (x * SQUARE_SIZE, y * SQUARE_SIZE))
            if (self.win(self.box.x, self.box.y, self.gate.x, self.gate.y)):
                screen.blit(win_image, (100, 100))
            pygame.display.flip()

    def loop(self):
            self.print_map()
