a, b = map(int, input().split())

# Please write your code here.
def cal(a,b):
    if a>b:
        a=a*2
        b=b+10
    else:
        b=b*2
        a=a+10
    return a,b
a,b=cal(a,b)
print(a,b)