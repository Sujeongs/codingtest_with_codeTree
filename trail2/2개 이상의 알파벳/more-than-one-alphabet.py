A = input()

# Please write your code here.
def st(a):
    if len(set(a))>=2:
        return "Yes"
    else:
        return "No"
    
print(st(A))
