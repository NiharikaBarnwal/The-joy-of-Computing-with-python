from PIL import Image
import random
end=100
def show_board():
    img = Image.open('NPTEL\week7\snake-and-ladder.jpg')
    img.show()

def check_ladder(points):
    if points==4:
        print('Ladder')
        return 25
    elif points==13:
        print('Ladder')
        return 46
    elif points==33:
        print('Ladder')
        return 49
    elif points==42:
        print('Ladder')
        return 63
    elif points==50:
        print('Ladder')
        return 69
    elif points==62:
        print('Ladder')
        return 81
    elif points==74:
        print('Ladder')
        return 92
    else:
        return points
    
def check_snake(points):
    if points==99:
        print('Snake')
        return 41
    elif points==89:
        print('Snake')
        return 53
    elif points==76:
        print('Snake')
        return 58
    elif points==66:
        print('Snake')
        return 45
    elif points==54:
        print('Snake')
        return 31
    elif points==43:
        print('Snake')
        return 18
    elif points==40:
        print('Snake')
        return 3
    elif points==27:
        print('Snake')
        return 5
    else:
        return points
    
def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1_name=input('Player 1, Enter your name : ')
    p2_name=input('Player 2, Enter your name : ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,'your turn')
            c = input('Press 1 to continue, 0 to quit : ')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game. Thanks for playing')
                break
            dice = random.randint(1,7)
            print('Dice showed',dice)
            pp1 = pp1+dice
            pp1 = check_ladder(pp1)
            pp1 = check_snake(pp1)
            # check if the player goes beyond the board
            if pp1> end:
                pp1=end
                print(p1_name,'Your score : ',pp1)
                print(p2_name,'Your score : ',pp2)
                if reached_end(pp1):
                    print(p1_name,'won')
                    break
        else:
            print(p2_name,'your turn')
            c = input('Press 1 to continue, 0 to quit : ')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game. Thanks for playing')
                break
            dice = random.randint(1,7)
            print('Dice showed',dice)
            pp2 = pp2+dice
            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)
            # check if the player goes beyond the board
            if pp2> end:
                pp2=end
                print(p2_name,'Your score : ',pp2)
                print(p1_name,'Your score : ',pp1)
                if reached_end(pp2):
                    print(p2_name,'won')
                    break
        turn=turn+1

show_board()
play()