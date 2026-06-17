n = int(input())

# Please write your code here.
class point:
    def __init__(self, x,y,num):
        self.x,self.y,self.num=x,y,num

po=[]

for i in range(n):
    x,y=map(int,input().split())
    po.append(point(x,y,i+1))

po.sort(key=lambda a:(abs(a.x)+abs(a.y)))

for i in po:
    print(i.num)
    