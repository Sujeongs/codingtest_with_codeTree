a, b = map(int, input().split())

# Please write your code here.
#소수인지 판별하는 함수
def prim(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

cnt=0
for i in range(a, b+1):
    if prim(i):
        if (i//10+i%10)%2==0:
            cnt+=1
print(cnt)