n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def ab(a):
    for i in a:
        print(abs(i),end=" ")
ab(arr)