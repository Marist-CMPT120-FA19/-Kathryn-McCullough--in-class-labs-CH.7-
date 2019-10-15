def work():

    hours=int(input("How many hours have you worked this week: "))
    rate= float(input("What is the hourly rate: "))
    normal_wage= float(rate*hours)
    overtime= int(hours-40)* float(rate*1.5)
    if hours <=(40):
        answer= float(normal_wage)
    elif hours > (40):
        answer= float((40*rate) + overtime)
    else:
        overtime=0

    print("Your pay is: $", float(answer))
work()




