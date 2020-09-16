input()
events = [int(x) for x in input().split()]
policePower = 0
untreatedCrimes = 0
for event in events:
    if event == -1:
        if policePower == 0:
            untreatedCrimes += 1
        else:
            policePower -= 1
    else:
        policePower += event

print(untreatedCrimes)
