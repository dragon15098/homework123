import random
import time
def in_map(x, y, screen_width, screen_height):
    if x < 0 or y < 0 or x > screen_width - 1 or y > screen_height - 1:
        return False
    return True

def win(bx, by, cpx, cpy):
    if((bx == cpx) and (by == cpy)):
        return True
    return False

def check_start(bx, by , cpx, cpy, px, py):
    if(bx == cpx) and (cpx == cpy):
        return True
    if(bx == px) and (by == py):
        return True
    return False

def move(x, y, dx, dy):
    return [x + dx, y + dy]
    
def check_box(bx, by, screen_width, screen_height, cpx, cpy):
    if win(bx, by, cpx,cpy):
        return False
    if((bx == cpx) and ((by != 0) or (by != screen_height -1 ))) or ((by == cpy) and ((bx != 0) or (bx != screen_width -1))):
        return False
    if(bx == 0) or (bx == screen_width - 1) or ( by == 0) or ( by == screen_height - 1):
        print("GAME OVER")
        return True
    return False

def p_g(px, py, cpx, cpy):
    if(px == cpx) and (px == cpy):
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

def play_or_exit():
    while True:
        choice = input("Play or Exit (P/E): ").upper()
        if(choice == "P"):
            return True
        elif(choice == "E"):
            return False
        else:
            print("Choice again: ") 

def undo(last_bx, last_by):
    return [last_bx,last_by]
count = 0
while play_or_exit():
    screen_width = random.randint(4,10)
    screen_height = random.randint(4,10)
    #n_box = int(input("how many box: "))
    px = random.randint(0,screen_width-1)
    py = random.randint(0,screen_height-1)
    bx = random.randint(1,screen_width - 2)
    by = random.randint(1,screen_height - 2)
    cpx = random.randint(0,screen_width-1)
    cpy = random.randint(0,screen_height-1)

    while p_g(px, py, cpx, cpy):
         px = random.randint(0,screen_width-1)
         py = random.randint(0,screen_height-1)

    while check_start(bx, by, cpx, cpy, px, py):
        bx = random.randint(1,screen_width - 2)
        by = random.randint(1,screen_height - 2)

    #px = 1
    #py = 1 
    #screen_width = 10
    #screen_height = 10
    #bx = 2
    #by = 2
    #cpx = 3
    #cpy = 3
    count = count +1 
    print("Stage", count)
    for i in range(3,0,-1):
        print (i)
        time.sleep(1) 
    while True:
        
        if win(bx, by, cpx, cpy):
            print ("YOU WIN")
            break

        for y in range(screen_height):
            for x in range(screen_width):
                if x == px and y == py:
                    print("P ", end="")
                elif x == bx and y == by:
                    print("B ", end="")
                elif x == cpx and y == cpy:
                    print("G ", end="")
                else:
                    print("- ", end="")
            print()
    
        start_time = time.time()
        choice = input("What do you want? W - S - A - D - U: ").upper()
        elapsed_time = time.time()-start_time
        if(elapsed_time > 2) and ((choice != "A") or (choice != "S") or (choice !="D") or (choice != "W")):
            print("GAME OVER. OUT OF TIME")
            break
        #if(choice == "U"):
        #    bx = last_bx
        #    by = last_by
        #    px = last_px
        #    py = last_py
        #else:
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
            last_bx = bx
            last_by = by
            last_px = px
            last_py = py

        if(check_box(bx, by, screen_width, screen_height, cpx, cpy)):
            break
        #print ( px, py, "        ", bx, by, "       ")
        #print ( last_px, last_by,"              " ,last_bx, last_by)
        
