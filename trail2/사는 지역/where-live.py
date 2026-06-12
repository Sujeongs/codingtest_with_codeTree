n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class P:
    def __init__(self, name, num, re):
        self.name=name
        self.num=num
        self.re=re
li=[]

for i in range(n):
    li.append(P(name[i],street_address[i], region[i]))

mx = li[0]

for i in li:
    if i.name > mx.name:
        mx = i

print("name", mx.name)
print("addr", mx.num)
print("city", mx.re)

