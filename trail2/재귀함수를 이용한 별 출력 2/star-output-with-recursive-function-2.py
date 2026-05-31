n = int(input())

# Please write your code here.n = int(input())

def recur(x):
    if x == 0:
        return
    
    print("* "*x, end=" ")
    print()
    recur(x - 1)
    print("* "*x, end=" ")
    print()

recur(n)