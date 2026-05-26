a, b = map(int, input().split())

# Please write your code here.
def cal(a,b):
    if a>b:
        a=a+25
        b=b*2
    else:
        b=b+25
        a=a*2
    return a,b
a,b=cal(a,b)
print(a,b)