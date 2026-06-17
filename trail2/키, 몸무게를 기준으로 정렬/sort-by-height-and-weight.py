n = int(input())

class per:
    def __init__(self, na, he,we):
        self.na, self.he, self.we=na,he,we

pe=[]
for _ in range(n):
    n_i, h_i, w_i = input().split()
    h_i=int(h_i) 
    w_i =int( w_i )
    pe.append(per(n_i, h_i, w_i))

pe.sort(key=lambda x:(x.he,-x.we))

for i in pe:
    print(i.na, i.he, i.we)