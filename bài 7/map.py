from player import Player
from box import Box
from gate import Gate 
class Map(object):
    """description of class"""
    def in_map(self, x, y, screen_width, screen_height):
        if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
            return False
        return True

    def __init__(self, width, height):
        self.player = Player(0, 0)
        self.box = Box(1,1)
        self.gate = Gate(2,2)
        self.width = width
        self.height = height

    #def print_map(boxes, p, gates, walls, screen_width, screen_height):
    def print_map(self):
        for y in range(self.height):
            for x in range(self.width):
                if (self.player.check_match(x, y)):
                    print("P", end=" ")
                elif self.box.check_match(x, y):
                    print("B", end=" ")
                elif self.gate.check_match(x, y):
                    print("G", end=" ")
                else:
                    print("-", end=" ")
            print()

    def move_player(self, dx, dy):
        self.player.nextx = self.player.x + dx
        self.player.nexty = self.player.y + dy
        self.box.nextx = self.box.x + dx
        self.box.nexty = self.box.y + dy
        if (self.in_map(self.player.nextx, self.player.nexty, self.width, self.height)):
            if self.box.check_match(self.player.nextx, self.player.nexty) and self.in_map(self.box.nextx, self.box.nexty, self.width, self.height):
                self.box.x = self.box.nextx
                self.box.y = self.box.nexty
                self.player.x = self.player.nextx
                self.player.y = self.player.nexty
            elif self.box.check_match(self.player.nextx, self.player.nexty):
                print("NO")
            else:
                self.player.x = self.player.nextx
                self.player.y = self.player.nexty
        else:
            print("NO")

    def player_input(self, direction):
        dx = 0
        dy = 0
        if direction == "w":
            dy = -1
        elif direction == "s":
            dy = 1
        elif direction == "a":
            dx = -1
        elif direction == "d":
            dx = 1
        self.move_player(dx, dy)


    def win(self, bx, by, gx, gy):
        if(bx == gx) and (by == gy):
            return True
        return False

    def loop(self):
        while True:
            self.print_map()
            direction = input("Your move (W,S,A,D): ")
            self.player_input(direction)
            if(self.win(self.box.x, self.box.y, self.gate.x, self.gate.y)):
               print("YOU WIN")
               break
            
