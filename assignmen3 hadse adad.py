import random
pcnumber=random.randint(0,20)
dafe= 0
while True:
    usernumber=int(input("enter number"))
    dafe += 1
    if pcnumber==usernumber:
        print("Barande")
        break
    if pcnumber<usernumber:
        print("paeentar")
    else:
        print("balatar")