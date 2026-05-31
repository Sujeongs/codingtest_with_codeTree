n = int(input())

def recur(x):
    if x == 0:
        return
    
    print(x, end=" ")
    recur(x - 1)
    print(x, end=" ")

recur(n)