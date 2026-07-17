def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    return result

base,exp = input("Enter base number and exponent: ").split()
base = int(base)
exp = int(exp)
print(f"{base}^{exp} is {exponent(base,exp)}")