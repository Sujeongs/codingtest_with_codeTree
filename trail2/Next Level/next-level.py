user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class code:
    def __init__(self,id="codetree",level=10):
        self.id=id
        self.level=level
two=code()
print("user",two.id,"lv",two.level)
one=code(user2_id, user2_level)
print("user",one.id,"lv",one.level)
