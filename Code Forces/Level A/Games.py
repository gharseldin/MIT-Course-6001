teams = int(input())
dictionaryOfHomeColors = {}
dictionaryOfAwayColors = {}
for i in range(teams):
    colors = input().split()
    dictionaryOfHomeColors[colors[0]
                           ] = dictionaryOfHomeColors.get(colors[0], 0) + 1
    dictionaryOfAwayColors[colors[1]
                           ] = dictionaryOfAwayColors.get(colors[1], 0) + 1
hostWearingAway = 0
for entry in dictionaryOfHomeColors:
    hostWearingAway += dictionaryOfHomeColors.get(
        entry) * dictionaryOfAwayColors.get(entry, 0)

print(hostWearingAway)
