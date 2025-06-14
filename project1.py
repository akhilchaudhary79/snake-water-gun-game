import random

'''
1 for snake
-1 for water
0 for gun
'''

# Fix: Use tuple for random.choice
computer = random.choice([0, 1, -1])

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Handle invalid input
if youstr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

if computer == you:
    print("It's a Draw")

elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
    print("You Win")

elif (computer == -1 and you == 0) or (computer == 1 and you == -1) or (computer == 0 and you == 1):
    print("You Lose")

else:
    print("Something went wrong")
