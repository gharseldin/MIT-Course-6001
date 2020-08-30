# I'm ignoring the first input cause practically
# I don't really need it
input()

games = input()
anton = 0
danik = 0
for ch in games:
    if ch == 'A':
        anton += 1
    else:   # this is based on the assumption that we either have A or D
        danik += 1

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
