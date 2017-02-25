def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def move(x, y, dx, dy):
    return [x + dx, y + dy]

def check_box(bx, by, screen_width, screen_height):
    if(bx == 0) or (bx == screen_width - 1) or ( by == 0) or ( by == screen_height - 1):
        print("GAME OVER")
        return True
    return False
def check_position(px, py, bx, by, choice):
    if(bx == px):
        if(by - py == 1) and (choice == 'S'):
            return True
        if(py - by == 1) and (choice == 'W'):
            return True
    if(by == py):
        if(px - bx == 1) and (choice == 'A'):
            return True
        if(bx - px == 1) and (choice == 'D'):
            return True
    return False

def win(bx, by, cpx, cpy):
    if((bx == cpx) and (by == cpy)):
        print("YOU WIN")
        return True
    return False

def play_or_exit():
    while True:
        choice = input("Play or Exit (P/E): ").upper()
        if(choice == "P"):
            return True
        elif(choice == "E"):
            return False
        else:
            print("Choice again: ")

while play_or_exit():
    px = 2
    py = 1
    bx = 1
    by = 1
    cpx = 4
    cpy = 6


    screen_width = 10
    screen_height = 10

    while not (win(bx, by, cpx, cpy)):
        for y in range(screen_height):
            for x in range(screen_width):
                if x == px and y == py:
                    print("P ", end="")
                elif x == bx and y == by:
                    print("B ", end="")
                elif x == cpx and y == cpy:
                    print("* ", end="")
                else:
                    print("- ", end="")
            print()
    
        choice = input("What do you want? W - S - A - D: ").upper()

        dx = 0
        dy = 0

        if choice == "W":
            dy = -1
        elif choice == "S":
            dy = 1
        elif choice == "A":
            dx = -1
        elif choice == "D":
            dx = 1

        if(check_position(px, py, bx, by, choice)):
           [next_bx, next_by] = move(bx, by, dx, dy)
        else: 
            next_bx = bx
            next_by = by
        [next_px, next_py] = move(px, py, dx, dy)

        if not in_map(next_px, next_py, screen_width, screen_height) or not in_map(next_bx, next_by, screen_width, screen_height) :
            print("Go away!!!")
        else:
            px = next_px
            py = next_py
            bx = next_bx
            by = next_by
        if(check_box(bx, by, screen_width, screen_height)):
            break
        
