player1 = ("Alex", 92)
player2 = ("Jordan", 92)

if player1[1] > player2[1]:
    print("Alex is the top player with ", player1[1], "points")
elif player1[1] == player2[1]:
    print("It's a tie")
else:
    print("Jordan is the top player with ", player2[1], "points")