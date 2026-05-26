A = input()

# Please write your code here.

def palindrome(a):
    string=a[::-1]
    return string

if A==palindrome(A):
    print("Yes")
else:
    print("No")
