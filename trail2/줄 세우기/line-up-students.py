n = int(input())

# Please write your code here.
class stu:
    def __init__(self,hi,we,num):
        self.hi,self.we,self.num=hi,we,num
st=[]
for i in range(n):
    student=tuple(map(int, input().split())) + (i + 1,)
    st.append(stu(*student))

st.sort(key=lambda x:(-x.hi,-x.we,x.num))

for i in st:
    print(i.hi, i.we,i.num)

