'''number = 1
while number < 11:
    print(number)
    number+=1

question_1 = int(input("Enter a number: "))
while question_1 > 0:
    print(question_1)
    question_1 -=1
print("BLAST OFF!")


total_sum = 0
question_2 = int(input("Enter a number as many times as you would like until you want to stop, enter 0: "))
while True:
    try:
        number = int(input("Enter a number as many times as you would like until you want to stop, enter 0: "))
        if number == 0:
            break
        total_sum += number
    except ValueError:
        print("Please enter a valid integer.")

print(f"Total sum: {total_sum}")


password = ("python123")
while True:
    try:
        guess = input("Enter your password: ")
        if guess == password:
            break
        else:
            print("Incorrect, Try again")
    except ValueError:
        print("please Enter a proper password")

print("Access Granted")
    
import random
number_to_guess = random.randint(1,10)
while True:
    try:
        guess_1 = int(input("Guess a number between 1 and 10: "))
        if guess_1 == number_to_guess:
            break
        elif guess_1 > number_to_guess:
            print("Too high!")
        else:
            print("Too low")
    except ValueError:
        print("Enter a proper number")

print("Correct!")
'''

number_2 = 2
while number_2 <= 20:
    print(number_2)
    number_2 += 2
    

  