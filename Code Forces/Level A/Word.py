word = input()
upper = 0
for character in word:
    if character.isupper():
        upper += 1
if upper * 2 > len(word):
    print(word.upper())
else:
    print(word.lower())
