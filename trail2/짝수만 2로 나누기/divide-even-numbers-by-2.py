n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def even(n, a):
    for i in range(n):
        if a[i]%2==0:
            a[i]=a[i]//2


even(n,arr)
for i in arr:
    print(i,end=" ")