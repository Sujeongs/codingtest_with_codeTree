n = int(input())

class student:
    def __init__(self, name, sc1, sc2, sc3):
        self.name, self.sc1, self.sc2, self.sc3=name, sc1, sc2, sc3

st=[]
for _ in range(n):
    student_input = input().split()
    student_input[1]=int(student_input[1])
    student_input[2]=int(student_input[2])
    student_input[3]=int(student_input[3])
    st.append(student(*student_input))

st.sort(key=lambda x: x.sc1 +x.sc2 + x.sc3)

for i in st:
    print(i.name, i.sc1, i.sc2, i.sc3)
# Please write your code here.
