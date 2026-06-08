secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class meet():
    def __init__(self, se,me,ti):
        self.se=se
        self.me=me
        self.ti=ti

meet1=meet(secret_code, meeting_point, time)
print("secret code :", meet1.se)
print("meeting point :", meet1.me)
print("time :", meet1.ti)