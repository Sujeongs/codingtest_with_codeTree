MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class na:
    def __init__(self, na, sc):
        self.na=na
        self.sc=sc

li = []

for i in range(MAX_N):
    li.append(na(codenames[i], scores[i]))

mn = li[0]

for i in li:
    if i.sc < mn.sc:
        mn = i

print(mn.na, mn.sc)


