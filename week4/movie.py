import random

movies=["BAGHBAAN","AVENGERS","SPIDERMAN","SUPERMAN","BARBIE","JUNGLEBOOK","ANAND",'DRISHYAM',"NAYAK","GOL MAAL","DANGAL","TAARE ZAMEEN PAR"]

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('_')
    qn=''.join(str(x)for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else: 
        return True
    
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==letter or ref[i]==' ':
            temp.append(ref[i])
        elif qn_list[i]=='_':
            temp.append('_')
        else:
            temp.append(ref[i])
    qn_new=''.join(str(x)for x in temp)
    return qn_new

def play():
    p1name=input("Enter 1st player name : ")
    p2name=input("Enter 2nd player name : ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            #player 1
            print(p1name,"Your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter : ").upper()
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('Press 1 to guess the movie or 2 to unlock another letter : '))
                    if d==1:
                        ans=input("Enter your answer : ").upper()
                        if ans==picked_movie:
                            pp1=pp1+1
                            print("Congrats!!!  It's correct.")
                            not_said=False
                            print(p1name,",Your score is : ",pp1)
                        else:
                            print("Wrong answer, Try again.")
                else:
                    print(letter,' not found')

        else:
            #player 2
            print(p2name,"Your turn")
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter : ").upper()
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=int(input('Press 1 to guess the movie or 2 to unlock another letter : '))
                    if d==1:
                        ans=input("Enter your answer : ").upper()
                        if ans==picked_movie:
                            pp2=pp2+1
                            print("Congrats!!!  It's correct.")
                            not_said=False
                            print(p2name,",Your score is : ",pp2)
                        else:
                            print("Wrong answer, Try again.")
                else:
                    print(letter,' not found')
        c=int(input("Press 1 to continue or 0 to quit : "))
        if c==0:
            print(p1name,"Your score:",pp1)
            print(p2name,"Your score:",pp2)
            print("Thanks for playing.")
            willing=False
        turn=turn+1
            
play()