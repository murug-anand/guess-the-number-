from random import randint
from art import logo
print(logo)
hard_life = 5

def numchecker(n):
    easy_life = n
    c = randint(1, 100)
    n = False
    while c != n:
        n = int(input("Enter Your Guess : "))
        if n > c:
            easy_life -= 1
            if easy_life <= 0:
                print(f"YOU LIFE is {easy_life} so you LOST")
                break
            print("too high")
            print(f"your remaining life is : {easy_life}")
        elif n < c:
            easy_life -= 1
            if easy_life <= 0:
                print(f"YOU LIFE is {easy_life} so you LOST")
                break
            print("too low")
            print(f"your remaining life is : {easy_life}")
        if n == c:
            print(f"YOU WON with {easy_life} LIFES remaining")


level = input("Which mode you wanna play EASY or HARD : ")
level = level.lower()
if level == "easy":
    numchecker(10)
elif level == "hard":
    numchecker(5)
else:
    print("please check u entered a valid mode")
