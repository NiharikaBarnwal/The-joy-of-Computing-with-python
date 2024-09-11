import random
def choose():
    words=["flower","watch","smile","mathematics","statistical","silicon","happiness","future","programming","coding"]
    return random.choice(words)

def jumble(word):
    return "".join(random.sample(word,len(word)))

def thank(player1,player2,pp1,pp2):
    print("Thank you for playing \n The score of ",player1, " is : " , pp1,"\nThe score of ",player2," is : ", pp2)
    print("Have a nice day!!!")
def play():
    player1 = input("player1, Enter your name: ")
    player2 = input("player2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #computer's task
        picked_word = choose()
        #create question
        qn = jumble(picked_word)
        print("The jumbled word is : ",qn)
        c=0
        #player1
        if turn%2==0:
            print(player1, ",your turn")
            ans=input("Guess the word : ")
            if ans==picked_word:
                pp1=pp1+1
                print("You guessed right!!!\nYour score is : ",pp1)
            else:
                print("Better luck next time! The word was : ",picked_word)
            c=int(input("Enter 1 to continue and 0 to quit : "))
        #player2
        else:
            print(player2,",your turn")
            ans=input("Guess the word : ")
            if ans==picked_word:
                pp2=pp2+1
                print("You guessed right!!!\nYour score is : ",pp2)
            else:
                print("Better luck next time! The word was : ",picked_word)
            c=int(input("Enter 1 to continue and 0 to quit : "))
        turn=turn+1
        if c==0:
            thank(player1,player2,pp1,pp2)
            break

play()