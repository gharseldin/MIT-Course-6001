input()
stones = input()
last = stones[0]
removed = 0
for i in range(1, len(stones)):
    if stones[i] == last:
        removed += 1
    else:
        last = stones[i]

print(removed)
