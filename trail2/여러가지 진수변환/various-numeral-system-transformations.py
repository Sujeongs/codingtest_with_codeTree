n, b = map(int, input().split())

if n == 0:
    print(0)
else:
    digits = []

    while n > 0:
        digits.append(str(n % b))
        n //= b

print(''.join(reversed(digits)))