unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class s:
    def __init__(self,un,wi,se):
        self.un=un
        self.wi=wi
        self.se=se

s1=s(unlock_code, wire_color, seconds)
print("code :", s1.un)
print("color :",s1.wi)
print("second :",s1.se)