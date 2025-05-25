number = input("Enter a number: ")

while True:
    try:
        number = int(number)
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        number = input("Enter a number: ")