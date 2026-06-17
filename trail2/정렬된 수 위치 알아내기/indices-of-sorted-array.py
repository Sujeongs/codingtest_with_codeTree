n = int(input())
sequence = list(map(int, input().split()))
s=[]
for i in range(n):
    s.append((i+1, sequence[i]))

# Please write your code here.
s.sort(key=lambda x:x[1])
result = [0] * (n+1)
for rank, item in enumerate(s):
    result[item[0]] = rank + 1  # 원래 위치에 정렬 후 순위 저장

for i in range(1, n+1):
    print(result[i], end=" ")
