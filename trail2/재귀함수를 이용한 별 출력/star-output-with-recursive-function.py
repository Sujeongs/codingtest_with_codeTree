n = int(input())

# Please write your code here.
def star(i):
    if i==0:
        return
        
    star(i-1)
    print('*'* i)

star(n)