num = int(input("enter your two digit number: "))

a = num // 10
b = num % 10

print(f"{a}^{b} =", a ** b)
print(f"{b}^{a} =", b ** a)