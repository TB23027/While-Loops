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

    
