input()
cards = [int(x) for x in input().split()]
i = 0
j = len(cards) - 1
players = [0, 0]
for x in range(len(cards)):
    if cards[i] > cards[j]:
        players[x % 2] += cards[i]
        i += 1
    else:
        players[x % 2] += cards[j]
        j -= 1

print(players[0], players[1])
