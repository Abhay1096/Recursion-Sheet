def digit(n):
    if n == 0:
        return 0
    else:
        return 1 + digit(n // 10)
n = int(input("Enter a number: "))
if n == 0:
    print(1)
else:
    print(digit(abs(n)))
