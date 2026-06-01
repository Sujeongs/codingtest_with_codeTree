b = int(input())

# Please write your code here.
def N(a):
    if a==1:
        return 1 
    return N(a-1) + a

print(N(b))