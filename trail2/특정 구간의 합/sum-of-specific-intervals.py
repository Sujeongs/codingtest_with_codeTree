n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for i in range(m):
    a1,a2=queries[i]
    sum=0
    for i in range(a1-1,a2):
        sum+=arr[i]
    print(sum)