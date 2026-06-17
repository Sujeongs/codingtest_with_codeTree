n = int(input())


# Please write your code here.
class stu:
    def __init__(self,h,w,n):
        self.h,self.w,self.n=h,w,n

st=[]
for i in range(n):
    h,w=map(int,input().split())
    st.append(stu(h,w,i+1))

st.sort(key=lambda x:(x.h,-x.w))

for i in st:
    print(i.h,i.w,i.n)