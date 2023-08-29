import random as ran
import time as ti

#x=10
x=int(input(f" Choose the upper limit of choices: "))

def randomchoice(up):
    user=0
    y=up+1
    choice="Y"
    
    while choice=="Y":
        comp_choice=ran.choice(range(1,y))
        while user != comp_choice:
            user = int(input(f" Choose a number between 1 and {up}: "))
            if 1<=user<y:
                if user<comp_choice:
                    print(f"Your choice {user} is lesser than computers choice. Choose higher!")
                else:
                    print(f"Your choice {user} is higher than computers choice. Choose lower!")
            else:
                print(f"Enter a valid number between 1 and {up}")
        
        print(f"Your choice {user} is equal to computers choice. Yaay!")
        ti.sleep(0.75)
        choice=input("Do you want to play again? Y or N: ")
    ti.sleep(0.5)
    print("Thanks for playing")
#y=int(x)
#if x.isdigit():
randomchoice(x)
#else:
#    print(f"Enter a valid number between 1 and {x}")