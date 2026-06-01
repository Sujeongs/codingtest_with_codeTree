N = int(input())

# Please write your code here.
def what(a):
    if a==1:
        return 0

    if a%2==0:
        
        return  what(a//2)+1
    else:
        return what(a//3)+1

print(what(N))