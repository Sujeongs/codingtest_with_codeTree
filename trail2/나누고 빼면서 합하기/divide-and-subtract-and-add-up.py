n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def pm(a):
    if a%2==1:
        a=a-1
    else:
        a=a//2
    return a
ans=0
while True:
    if m<1:
        break
    ans+=A[m-1]
    m=pm(m)
print(ans)