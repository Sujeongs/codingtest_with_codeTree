N = int(input())

# Please write your code here.
def s(a):
    if a<10:
        return a**2
    return s(a//10)+ (a%10)**2
print(s(N))