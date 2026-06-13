n = 5


class infor:
    def __init__(self,n,h, w):
        self.n,self.h, self.w=n,h, w

i=[]
for _ in range(n):
    n, h, w = input().split()
    h=int(h)
    w=float(w)
    i.append(infor(n,h,w))
i.sort(key=lambda x:x.n)

print("name")
for a in i:
    print(a.n,a.h,a.w)
print()
print("height")
i.sort(key=lambda x:-x.h)
for a in i:
    print(a.n,a.h,a.w)
