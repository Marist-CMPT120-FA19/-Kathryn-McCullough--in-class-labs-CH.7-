def credits():

    credit=int(input("How many credits do you have: "))
    if credit< (7):
        answer= "Freshman"
    elif credit <=(15):
        answer= "Sophmore"
    elif credit <=(25):
        answer= "Junior"
    elif credit >= (26):
        answer= "Senior"
    else:
        answer= "Did you even go to school?"


    print("You are a:", answer)

credits()
