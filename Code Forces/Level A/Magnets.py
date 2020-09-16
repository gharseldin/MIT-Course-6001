magnets = int(input())
groups = 1
end = input()
for i in range(1, magnets):
    magnet = input()
    if end[1] == magnet[0]:
        groups += 1
    end = magnet
print(groups)
