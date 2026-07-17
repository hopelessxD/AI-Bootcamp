def factorial(num):
    fac = 1
    for val in range(1, num + 1):
        fac = fac * val
    return fac


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"factorial of {num} is {factorial(num)}")