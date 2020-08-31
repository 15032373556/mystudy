print("Give me two numbers,and I will add them up.")
print("Enter 'q' to quit.")

while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        fn = int(first_number)
        second_number = input("\nSecond number: ")
        if second_number == 'q':
            break
        sn = int(second_number)
    except ValueError:
        print("You have entered text, please enter numbers")
    else:
        answer = fn + sn
        print(answer)

