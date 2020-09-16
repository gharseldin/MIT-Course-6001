name = input()
letterDictionary = {}
for character in name:
    letterDictionary[character] = letterDictionary.get(character, 0) + 1
if len(letterDictionary) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
