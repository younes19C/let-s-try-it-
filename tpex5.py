def Pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_result = Pgcd(num1, num2)
print("The greatest common divisor of", num1, "and", num2, "is", gcd_result)                             