class student:
    def __init__(self,n,k,e,m):
        self.n,self.k,self.e,self.m=n,k,e,m

n = int(input())


stu=[]
for _ in range(n):
    student_info = input().split()
    student_info[1]=int(student_info[1])
    student_info[2]=int(student_info[2])
    student_info[3]=int(student_info[3])
    stu.append(student(*student_info))
# Please write your code here.

stu.sort(key=lambda x:(-x.k,-x.e,-x.m))

for i in stu:
    print(i.n, i.k, i.e, i.m)