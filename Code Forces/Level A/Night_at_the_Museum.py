word = input()
position = 0
moves = 0
for character in word:
    newPosition = ord(character) - ord('a')
    if abs(newPosition - position) <= 13:
        moves += abs(newPosition - position)
    else:
        moves += 26 - abs(newPosition - position)
    position = newPosition

print(moves)
