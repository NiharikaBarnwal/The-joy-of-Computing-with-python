import string
import random
symbols = []
symbols = list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
# pos1 ans po2 are position of the same symbol in card1 and card2 resp
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if pos1==pos2:
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while (i<5):
    if (i!=pos1 and i!=pos2):
        card1[i]=random.choice(symbols)
        symbols.remove(card1[i])
        card2[i]=random.choice(symbols)
        symbols.remove(card2[i])
    i=i+1
print("Card1 : ","".join(random.sample(card1,len(card1))))
print("Card2 : ","".join(random.sample(card2,len(card2))))

ans=input("Enter the simlar symbol : ")
if ans==samesymbol:
    print("Yay!! You are correct.")
else:
    print("Try again next time. :(")