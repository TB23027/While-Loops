number = 1
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


number_2 = 2
while number_2 <= 20:
    print(number_2)
    number_2 += 2


number_3 = int(input("Enter a number: "))
times = 1
while times <=10:
    print(f"{number_3} x {times} = {number_3 * times} ")
    times += 1




while True:
    try:
        guess = int(input("Enter a number: "))
        if guess <= 100 and guess >= 0:
            break
        else:
            print("Invalid, Try again")

    except ValueError:
        print("Please enter a valid number: ")
    
print("Accepted")



question_4 = input("Enter a word: ")
vowels = "aeiouAEIOU"
result = ""
index = 0
while index < len(question_4):
    if question_4[index] not in vowels:
        result += question_4[index]
    
    index += 1
print("Word without vowels:", result)


number_4 = int(input("Enter a number: "))
factorial = 1
while number_4 > 0:
    factorial *= number_4
    number_4 -= 1
print("Factorial is", factorial)



  