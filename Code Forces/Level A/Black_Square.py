calories = [int(x) for x in input().split()]
gameLines = input()
caloriesConsumed = 0
for line in gameLines:
    caloriesConsumed += calories[int(line)-1]
print(caloriesConsumed)
