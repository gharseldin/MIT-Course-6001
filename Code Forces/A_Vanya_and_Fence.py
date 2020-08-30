n, h = (int(x) for x in input().split())
heights = [int(x) for x in input().split()]

width = 0
for height in heights:
    if height > h:
        width += 2
    else:
        width += 1

print(width)
