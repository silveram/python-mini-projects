import sys, random, time
wins=0
losses=0
ties=0
user_inputs={
    "r":"Rock",
    "s":"Scissors",
    "p":"Papers"
    }
print("""Greetings!,
This is a Rock, Paper, Scissors game, plain and simple 
""")
try:
    while True:
        print()
        print("***The current score is ", wins ,"wins",losses,"losses",ties,"ties","***")
        print("******To start the game enter your move: (r)ock (p)aper (s)cissors, to quit press (q)uit ******")
        #user input verification
        while True :
            user=input()
            if user not in ["r","p","s","q"]:
                print("you did not enter a valid move")
                continue
            else:
                break
                
        if user=="q":
            print("Thank you for playing")
            sys.exit()
        print("you have chosen",user_inputs[user])
        #computer choice generation
        computer_choice_generator=random.randint(1,30)
        for i in range(6):
            print("*", end="")
            time.sleep(0.5)
        print()    
        if computer_choice_generator<=10:
            computer_choice="r"
            print("Computer has chosen rock; therefore,", end=" ")
        elif 10<computer_choice_generator<=20:
            computer_choice="p"
            print("Computer has chosen paper; therefore,", end=" ")
        else:
            computer_choice="s"
            print("Computer has chosen scissors; therefore,", end=" ")
        #deciding the outcome of the game
        if user==computer_choice:
            ties+=1
            print("you are tied")
            print()
            time.sleep(1) #to artificially slow the game as it's too fast
            continue   #no need to continue to the rest of the script
        else:
            if user=="r" and computer_choice=="s" or user=="p" and computer_choice=="r" or user=="s" and computer_choice=="p" :
                wins+=1
                print("you are victorious")
            else :
                losses+=1
                print(" you have lost")
        time.sleep(1) #to artificially slow the game as it's too fast
except:    
    print("An Error has occured")
    
             
        
