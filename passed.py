count = 0

for _ in range(10):
    user_input = input("Enter a number (1 or 2): ")

    if user_input == '1':
        count += 1
        if count > 8:
            print("Bonus to the teacher")

    elif user_input == '2':
        print("The student failed")
        break

    else:
        print("Invalid input. Please enter either 1 or 2.")


