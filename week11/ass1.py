date=input("Enter the date (MM/DD/YYYY):")
d1=date.split("/")
d1[0],d1[1]=d1[1],d1[0]
d1[2]=d1[2][2:]
print("Given date (DD-MM-YY):","-".join(d1))