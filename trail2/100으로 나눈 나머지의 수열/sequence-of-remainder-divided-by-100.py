N = int(input())

# Please write your code here.
def ad(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (ad(n-1)*ad(n-2))%100
print(ad(N))