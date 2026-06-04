N = int(input())

# Please write your code here.
def fa(a):
    if a==0 or a==1:
        return 1

    return a * fa(a-1)

print(fa(N))