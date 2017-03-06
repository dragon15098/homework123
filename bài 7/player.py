class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def next_position(self, dx, dy):
        return [self.x + dx, self.y + dy]

    def check_match(self, x, y):
        if self.x == x and self.y == y:
            return True
        return False
