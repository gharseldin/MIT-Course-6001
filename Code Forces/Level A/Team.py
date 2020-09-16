questionsAsked = int(input())
questionsSolved = 0
for i in range(questionsAsked):
    poll = 0
    for x in input().split():
        poll += int(x)
    if poll > 1:
        questionsSolved += 1
print(questionsSolved)
