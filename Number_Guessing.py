import random
n = random.randint(1, 100)
a =-1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("Guess the number : "))
    if(a>n):
        print("lower number plese")
    else:
        print("Higher number plese")
        
print(f"You have guseed the number correctly in {guesses} attempt")

    