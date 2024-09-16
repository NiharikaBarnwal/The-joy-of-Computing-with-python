def move_player(ladders,snakes,current_position,die_roll):
    current_position=current_position+die_roll
    if current_position in ladders:
        return 1
    elif current_position in snakes:
        return -1
    else:
        return 0
    

ladders=list(map(int,input("Enter the blocks containing ladders : ").split()))
snakes=list(map(int,input("Enter the blocks containing snakes : ").split()))
current_position=int(input("Enter the current position: "))
die_roll=int(input("Enter the number on the dice: "))
print(move_player(ladders,snakes,current_position,die_roll))


