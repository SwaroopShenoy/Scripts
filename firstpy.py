import time as t

name=input("What is your name? ")

height=int(input("What is your height?(in cm) "))

print(f"Hello {name}, Are you {height} cm tall? ")
feed = input("1 is yes, 2 is no. Enter a choice: ")
while feed != "":
    if feed == "1":
        height2 = float(height/2.54)
        height3 = int(height2/12)
        height4 = int(height2%12)
        print("Calculating...")
        t.sleep(0.5)
        print(f"You are {height2:.0f} inches tall, that is {height3}\'{height4}\" ") 
        quit()
    else:
        print("Sorry")


#print("Good Job Me!")