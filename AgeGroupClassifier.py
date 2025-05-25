while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            continue # Loop back to ask for age again
        elif age < 13:
            print("You are a child.")
        elif age < 20:
            print("You are a teenager.")
        elif age < 65:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")
        age = input("Enter your age: ")