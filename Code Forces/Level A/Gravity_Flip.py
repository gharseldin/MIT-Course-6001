input()
blocks = [int(x) for x in input().split()]
blocks.sort()
print(' '.join(str(x) for x in blocks))
