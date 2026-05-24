a, b = map(int, input().split())

# Please write your code here.

def dhswjstn(a):
    if a%2==0 or a%10==5 or (a%3==0 and a%9!=0):
        return False
    else:
        return True

cnt=0

for i in range(a,b+1):
    if dhswjstn(i):
        cnt+=1
print(cnt)