import random
import sys


FIRST_POSITION_LIST = [0,1,2,3]
SECOND_POSITION_LIST = [0,1,2,3]

           
def up_movement(game_box):
    i = 0
    for j in range(0,4):
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0:
            if game_box[i][j] == 0:
                while game_box[i][j] == 0:
                    game_box[i][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0
            
            if game_box[i+1][j]==0 and (game_box[i+2][j]!=0 or game_box[i+3][j]!=0):
                while game_box[i+1][j] == 0:
                    game_box[i+1][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0

            if game_box[i+2][j] == 0 and game_box[i+3][j]!=0:
                while game_box[i+2][j] == 0:
                    game_box[i+2][j] = game_box[i+3][j]
                    game_box[i+3][j] = 0

def up_addition(game_box, points):
    i = 0
    for j in range(0,4):
        if game_box[i][j] == game_box[i+1][j]:
            game_box[i][j] = game_box[i][j] + game_box[i+1][j]
            points += game_box[i][j] ** 2
            game_box[i+1][j] = game_box[i+2][j]
            game_box[i+2][j] = game_box[i+3][j]
            game_box[i+3][j] = 0

        if game_box[i+1][j] == game_box[i+2][j]:
            game_box[i+1][j] = game_box[i+1][j] + game_box[i+2][j]
            points += game_box[i+1][j] ** 2
            game_box[i+2][j] = game_box[i+3][j]
            game_box[i+3][j] = 0

        if game_box[i+2][j] == game_box[i+3][j]:
            game_box[i+2][j] = game_box[i+2][j] + game_box[i+3][j]
            points += game_box[i+2][j] ** 2
            game_box[i+3][j] = 0
    return points
def up_check(game_box):
    for j in range(0,4):
        for i in range(0,3):
            if game_box[i][j] == game_box[i+1][j]:
                return True
            else:
                return False            


def down_movement(game_box):
    i = 0
    for j in range(0,4):
        if game_box[i][j]!=0 or game_box[i+1][j]!=0 or game_box[i+2][j]!=0 or game_box[i+3][j]!=0:
            if game_box[i+3][j] == 0:
                while game_box[i+3][j] == 0:
                    game_box[i+3][j] = game_box[i+2][j]
                    game_box[i+2][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0
            
            if game_box[i+2][j] == 0 and (game_box[i+1][j]!=0 or game_box[i][j]!=0):
                while game_box[i+2][j] == 0:
                    game_box[i+2][j] = game_box[i+1][j]
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i+1][j] == 0 and game_box[i][j] !=0:
                while game_box[i+1][j] == 0:
                    game_box[i+1][j] = game_box[i][j]
                    game_box[i][j] = 0

def down_addition(game_box, points):
    i = 0
    for j in range(0,4):
        if game_box[i+3][j] == game_box[i+2][j]:
            game_box[i+3][j] = game_box[i+3][j] + game_box[i+2][j]
            points += game_box[i+3][j] ** 2
            game_box[i+2][j] = game_box[i+1][j]
            game_box[i+1][j] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i+2][j] == game_box[i+1][j]:
            game_box[i+2][j] = game_box[i+2][j] + game_box[i+1][j]
            points += game_box[i+2][j] ** 2
            game_box[i+1][j] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i+1][j] == game_box[i][j]:
            game_box[i+1][j] = game_box[i+1][j] + game_box[i][j]
            points += game_box[i+1][j] ** 2
            game_box[i][j] = 0
    return points
def down_check(game_box):
    for j in range(0,4):
        for i in range(0,3):
            if game_box[i+3][j] == game_box[i+2][j]:
                return True
            else:
                return False            
       

def left_movement(game_box):
    j = 0
    for i in range(0,4):
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0:
            if game_box[i][j] == 0:
                while game_box[i][j] == 0:
                    game_box[i][j] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0
            
            if game_box[i][j+1] == 0 and (game_box[i][j+2]!=0 or game_box[i][j+3]!=0):
                while game_box[i][j+1] == 0:
                    game_box[i][j+1] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0

            if game_box[i][j+2] == 0 and game_box[i][j+3] !=0:
                while game_box[i][j+2] == 0:
                    game_box[i][j+2] = game_box[i][j+3]
                    game_box[i][j+3] = 0
       
def left_addition(game_box, points):
    j = 0
    for i in range(0,4):
        if game_box[i][j] == game_box[i][j+1]:
            game_box[i][j] = game_box[i][j] + game_box[i][j+1]
            points += game_box[i][j] ** 2
            game_box[i][j+1] = game_box[i][j+2]
            game_box[i][j+2] = game_box[i][j+3]
            game_box[i][j+3] = 0

        if game_box[i][j+1] == game_box[i][j+2]:
            game_box[i][j+1] = game_box[i][j+1] + game_box[i][j+2]
            points += game_box[i][j+1] ** 2
            game_box[i][j+2] = game_box[i][j+3]
            game_box[i][j+3] = 0

        if game_box[i][j+2] == game_box[i][j+3]:
            game_box[i][j+2] = game_box[i][j+2] + game_box[i][j+3]
            points += game_box[i][j+2] ** 2
            game_box[i][j+3] = 0
    return points    
def left_check(game_box):
    for i in range(0,4):
        for j in range(0,3):
            if game_box[i][j] == game_box[i][j+1]:
                return True
            else:
                return False            


def right_movement(game_box):
    j = 0
    for i in range(0,4):
        if game_box[i][j]!=0 or game_box[i][j+1]!=0 or game_box[i][j+2]!=0 or game_box[i][j+3]!=0:
            if game_box[i][j+3] == 0:
                while game_box[i][j+3] == 0:
                    game_box[i][j+3] = game_box[i][j+2]
                    game_box[i][j+2] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0
            
            if game_box[i][j+2] == 0 and (game_box[i][j+1]!=0 or game_box[i][j]!=0):
                while game_box[i][j+2] == 0:
                    game_box[i][j+2] = game_box[i][j+1]
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0

            if game_box[i][j+1] == 0 and game_box[i][j] !=0:
                while game_box[i][j+1] == 0:
                    game_box[i][j+1] = game_box[i][j]
                    game_box[i][j] = 0
            
def right_addition(game_box, points):
    j = 0
    for i in range(0,4):
        if game_box[i][j+3] == game_box[i][j+2]:
            game_box[i][j+3] = game_box[i][j+3] + game_box[i][j+2]
            points += game_box[i][j+3] ** 2
            game_box[i][j+2] = game_box[i][j+1]
            game_box[i][j+1] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i][j+2] == game_box[i][j+1]:
            game_box[i][j+2] = game_box[i][j+2] + game_box[i][j+1]
            points += game_box[i][j+2] ** 2
            game_box[i][j+1] = game_box[i][j]
            game_box[i][j] = 0

        if game_box[i][j+1] == game_box[i][j]:
            game_box[i][j+1] = game_box[i][j+1] + game_box[i][j]
            points += game_box[i][j+1] ** 2
            game_box[i][j] = 0
    return points
def right_check(game_box):
    for i in range(0,4):
        for j in range(0,3):
            if game_box[i][j+3] == game_box[i][j+2]:
                return True
            else:
                return False            


def getchar():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def prRed(prt): print("\033[91;40m {} \033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prBrightBlue(prt): print("\033[34m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))

def game_play():
    points = 0
    game_box = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    first_row_to_begin = random.choice(FIRST_POSITION_LIST)
    first_column_to_begin = random.choice(FIRST_POSITION_LIST)
    game_box[first_row_to_begin][first_column_to_begin] = 2

    second_row_to_begin = random.choice(SECOND_POSITION_LIST)
    second_column_to_begin = random.choice(SECOND_POSITION_LIST)
    game_box[second_row_to_begin][second_column_to_begin] = 2

    while True:
        prBrightBlue('Moves: "w"=up, "s"=down, "a"=left, "d"=right')
        prGreen("Points: " + str(points))          
        print(game_box[0][0], '\t', game_box[0][1], '\t', game_box[0][2], '\t', game_box[0][3], '\n')
        print(game_box[1][0], '\t', game_box[1][1], '\t', game_box[1][2], '\t', game_box[1][3], '\n')
        print(game_box[2][0], '\t', game_box[2][1], '\t', game_box[2][2], '\t', game_box[2][3], '\n')
        print(game_box[3][0], '\t', game_box[3][1], '\t', game_box[3][2], '\t', game_box[3][3], '\n')
        prBrightBlue('Choose your movement or press "q" to exit: ')

        movement_choice = getchar()

        if movement_choice == 'w':
            up_movement(game_box)
            points = up_addition(game_box, points)
        elif movement_choice == 's':
            down_movement(game_box)
            points = down_addition(game_box, points)
        elif movement_choice == 'a':
            left_movement(game_box)
            points = left_addition(game_box, points)
        elif movement_choice == 'd':
            right_movement(game_box)
            points = right_addition(game_box, points)
        elif movement_choice == 'q':
            exit()
        else:
            invalid_input = 0
            invalid_input += 1
            continue
        
        row_indexes_with_zero = []
        column_indexes_with_zero = []

        for i in range(0,4):
            for j in range(0,4):
                if game_box[i][j] == 0:              
                    row_indexes_with_zero.append(i)
                    column_indexes_with_zero.append(j)
                elif game_box[i][j] == 8:
                    print(game_box[0][0], '\t', game_box[0][1], '\t', game_box[0][2], '\t', game_box[0][3], '\n')
                    print(game_box[1][0], '\t', game_box[1][1], '\t', game_box[1][2], '\t', game_box[1][3], '\n')
                    print(game_box[2][0], '\t', game_box[2][1], '\t', game_box[2][2], '\t', game_box[2][3], '\n')
                    print(game_box[3][0], '\t', game_box[3][1], '\t', game_box[3][2], '\t', game_box[3][3], '\n')
                    prYellow('Congratulations, you are the CHICKEN WINNER! ')
                    prGreen('Total points: ' + str(points))
                    exit()

        if len(row_indexes_with_zero) > 1:
            random_index = row_indexes_with_zero.index(random.choice(row_indexes_with_zero))
            row_to_place_item = row_indexes_with_zero[random_index]
            column_to_place_item = column_indexes_with_zero[random_index]
            game_box[row_to_place_item][column_to_place_item] = 2
        elif len(row_indexes_with_zero) == 1:
            row_to_place_item = row_indexes_with_zero[0]
            column_to_place_item = column_indexes_with_zero[0]
            game_box[row_to_place_item][column_to_place_item] = 2
        elif up_check(game_box) or down_check(game_box) or left_check(game_box) or right_check(game_box):
            continue
        elif len(row_indexes_with_zero) == 0:
            break

    prGreen('Total points: ' + str(points))
    prRed('GAME OVER!!4! But... Thanks for playing! ;-) ')

def play_again():
    again = str(input("Do you want to play again? Y/n :"))
    if again == "n":
        return False
    elif again == "Y":
        return True  
    else:
        print("Not a valid answer!")

def main():
    while True:
        game_play()
        if not play_again():
            return

if __name__ == '__main__':
    main()
    print("Bye-bye")
    exit()
