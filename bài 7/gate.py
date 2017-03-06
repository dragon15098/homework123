class Gate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def check_match(self, x, y):
        if self.x == x and self.y == y:
            return True
        return False
