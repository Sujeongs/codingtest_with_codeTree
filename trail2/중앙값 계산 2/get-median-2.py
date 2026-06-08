n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(1,n+1,2):
    new=sorted(arr[:i])
    print(new[i//2],end=" ")