N = int(input())

# Please write your code here.
def tw(a):
    if a==1 or a==2:
        return a
    if a%2==0:
        return a+tw(a-2)
    else:
        return a+tw(a-2)

print(tw(N))