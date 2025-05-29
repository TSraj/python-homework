favourite_colors = ("red", "green", "blue", "yellow", "purple")

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = input("Guess one of my favourite colors: ")
    if guess in favourite_colors:
        print("Correct! That's one of my favourite colors.")
    else:
        print("Incorrect. Try again!")
        attempts += 1

if attempts == max_attempts:
    print("Sorry, you've used all your attempts. My favourite colors are:", ", ".join(favourite_colors))