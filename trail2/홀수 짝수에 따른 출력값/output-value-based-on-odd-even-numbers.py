N = int(input())

# Please write your code here.
def tw(a):
    if a==1 or a==2:
        return a

    return a+tw(a-2)
    

print(tw(N))