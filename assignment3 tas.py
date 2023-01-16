import random
while True:
    t=input("enter 's' for start and enter 'q' for exit :")
    if t=='s':
        tas=random.randint(1,6)
        if 1<=tas<=5:
            print("tas=", tas)
    if tas==6:
        tas1=random.randint(1,6)
        tas2=random.randint(1,6)
        print("barande tas=6, jayeze tas1= ",tas1, "jayeze tas2= ", tas2)
    if t=='q':
        print("tamam")
        break