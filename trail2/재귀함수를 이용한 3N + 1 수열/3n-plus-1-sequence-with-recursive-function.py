n = int(input())

# Please write your code here.
def ad(n):
    if n==1:
        return 0
    if n%2==0:
        n=n//2
        return 1+ad(n)
    else:
        n=n*3+1
        return 1+ad(n)
print(ad(n))