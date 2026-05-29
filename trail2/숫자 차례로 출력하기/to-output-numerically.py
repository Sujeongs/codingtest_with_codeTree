n = int(input())

def one_to_n(x):
    if x == 0:
        return
    
    one_to_n(x - 1)
    print(x, end=" ")

def n_to_one(x):
    if x == 0:
        return
    
    print(x, end=" ")
    n_to_one(x - 1)

one_to_n(n)
print()
n_to_one(n)