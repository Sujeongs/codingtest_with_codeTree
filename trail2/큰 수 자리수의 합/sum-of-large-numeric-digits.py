a, b, c = map(int, input().split())

# Please write your code here.
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(a * b * c))