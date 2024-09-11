def rps(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if player1[p1]==player2[p2]:
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor") or (player1[p1]=="Paper" and player2[p2]=="Rock") or (player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print("Player1 wins!!!")
    else:
        print("Player2 wins!!!")
player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Paper',1:'Rock',2:'Scissor'}
while(1):
    num1=input("Player 1, Enter your choice : ")
    num2=input("Player 2, Enter your choice : ")
    bit1=int(input("Player 1, Enter the secret bit position : "))
    bit2=int(input("Player 2, Enter the secret bit position : "))
    rps(num1,num2,bit1,bit2)
    ch=input("Do you want to continue? y/n : ")
    if(ch=='n'):
        break