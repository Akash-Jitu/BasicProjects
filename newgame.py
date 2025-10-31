
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake" , -1: "water", 0: "gun"}
you = youdict[youstr]
print(f"You chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")
if(computer == you):
    print("It's a Draw !")
    
else:
    if(computer == -1 and you == 1):
        print("You win !!!")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win !!!")
    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 1 and you == -1):
        print("You win")
    elif(computer == 1 and you == 0):
        print("You lose") 
    else:
        print("Something went wrong")   
        
    