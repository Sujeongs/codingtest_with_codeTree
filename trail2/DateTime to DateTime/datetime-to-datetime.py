a, b, c = map(int, input().split())

# Please write your code here.
day=11
hour=11
min=11

e_t=0

while True:
    if a==day and b==hour and c==min:
        break
    elif a<day and b<hour and c<min:
        e_t=-1
        break

    e_t+=1
    min+=1
    if min==60:
        hour+=1
        min=0
    if hour==24:
        day+=1
        hour=0
print(e_t)