n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.


new_li=[]

for i in str:
    if i[0:len(t)]==t:
        new_li.append(i)
        
new_li.sort()
print(new_li[k-1])