n = int(input())
name = []
height = []
weight = []

class per:
    def __init__(self, n_i,h_i,w_i):
        self.n_i=n_i
        self.h_i=h_i
        self.w_i=w_i
person=[]
for _ in range(n):
    n_i, h_i, w_i = input().split()
    person.append(per(n_i, h_i, w_i))
    # name.append(n_i)
    # height.append(int(h_i))
    # weight.append(int(w_i))
person.sort(key=lambda x:x.h_i )
for persona in person:
    print(persona.n_i, persona.h_i,persona.w_i)
