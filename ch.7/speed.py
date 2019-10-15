def speed():
    speed=eval(input("What is your speed?: "))
    limit=eval(input("What is the speed limit?: "))


    if speed> (90):
        return print("You will be fined $200 for speeding over 90 mph. Your speed was illegal and you will recieve a speeding ticket fine of $", 50 + (speed-limit)*5)
    elif speed> limit:
        return print("Your speeding ticket fine is $", 50 + (speed-limit)*5)
    else:
        return print("Your speed was legal.")
speed()
    
        
        
            
