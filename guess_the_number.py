import sys, time, random

print("""In this game you try to guess the number that will be generated by the computer.It'll an interger.
You will choose how many tries you'll have to figure the number and the interval the number is in.
Please provide an integer or press q to quit the game""")

#user input validation
def user_valid():
    while True:
        user_input=input()
        try:
            type(int(user_input)) 
        except :
            print("please provide an integer")
            continue
        if type(int(user_input))== int:
            break
    return int(user_input)
while True:
    print("please provide lowest and highest values of the internal you wish to guess the number in")
    #Acquiring the limits of the interval and verifying that lowest value is lesser than highest value
    while True:
        print("Highest value is: ", end="")
        highest=user_valid()
        print("lowest value is: ", end="")
        lowest=user_valid()
        if highest<lowest:
            print("Highest value should be greater than lowest value")
            continue
        else:
            break
    print("number of desired trials: ", end="")
    trials=user_valid()
    #the game
    computer=random.randint(lowest,highest)
    print("what is your guess: ", end="")
    for i in range(trials):
        user_guess=user_valid()
        if user_guess<computer:
            print("it's lower, try again", trials-i-1,"trials are left")
        elif user_guess>computer:
            print("it's higher, try again", trials-i-1,"trials are left")
        else:
            print("Bingo you've found it")
            break
        if trials-i-1==0:
            print("Unfortunately, you,ve lost")
    
    print("To retry enter r and any other key to quit")
    game_continuation=input()
    if game_continuation=="r":
        continue
    else:
        sys.exit()
       
