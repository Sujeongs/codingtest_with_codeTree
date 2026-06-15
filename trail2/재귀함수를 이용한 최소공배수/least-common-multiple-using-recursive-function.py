n = int(input())
arr = list(map(int, input().split()))
a=0
# Please write your code here.
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)
if n==1:
    a=arr[0]
else:
    for i in range(1,n):
        if i==1:
            a=lcm(arr[i-1],arr[i])
        else:
            a= lcm(a,arr[i])
print(a)