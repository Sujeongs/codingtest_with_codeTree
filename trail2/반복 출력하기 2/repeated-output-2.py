n = int(input())

# Please write your code here.
def N(n):
    if n==0:
        return
    print("HelloWorld")
    N(n-1)

N(n)