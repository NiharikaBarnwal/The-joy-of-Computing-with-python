import random
import matplotlib.pyplot as plt
account=0
x=[]
y=[]
for i in range(365):
    x.append(i+1)
    bet=random.randint(1,11)
    lucky_draw=random.randint(1,11)
    #print("Bet : ",bet)
    #print("Lucky draw : ",lucky_draw)
    if bet==lucky_draw:
        account=account+900-100
    else:
        account=account-100
    y.append(account)
print("Ammount in your game account : ",account)
plt.plot(x,y)
plt.show