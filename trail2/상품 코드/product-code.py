product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class code:
    def __init__(self, pro="codetree",co=50):
        self.pro=pro
        self.co=co

one=code()
print("product", one.co,"is", one.pro)
two=code(product_name, product_code)
print("product", two.co,"is", two.pro)