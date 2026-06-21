n = int(input())
a = [int(input()) for _ in range(n)]

cnt = 1
max_cnt = 1
for i in range(1, n):
    if a[i] == a[i - 1]:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        cnt = 1

print(max_cnt)