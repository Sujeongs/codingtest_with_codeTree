M, D = map(int, input().split())

# Please write your code here.
mon={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if 1<=M<=12 and 1<=D<=mon[M]:
    print("Yes")
else:
    print("No")