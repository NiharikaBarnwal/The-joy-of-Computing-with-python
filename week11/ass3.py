dict={'a':'0','k':'1','x':'2','y':'3','s':'4','m':'5','b':'6','d':'7','p':'8','z':'9'}
coded_date=input("Enter the encoded date:")
decoded_date=""
for i in coded_date:
    if i.isalpha():
        if i in dict:
            decoded_date+=dict[i]
        else:
            print("Invalid date")
    else:
        decoded_date+=i
print(decoded_date)