row = 0
column = 0
for i in range(5):
    inputRow = input().split()
    for j in range(5):
        if inputRow[j] == '1':
            row = i
            column = j
            break

# since we want to move the 1 to row 2 and column 2
print(abs(2-row) + abs(2-column))
