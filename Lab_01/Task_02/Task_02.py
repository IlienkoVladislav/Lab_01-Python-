num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))
num3 = float(input("Enter the first floating-point number: "))
num4 = float(input("Enter the second floating-point number: "))

print("First integer number:", num1)
print("Second integer number:", num2)
print("First floating-point number:", num3)
print("Second floating-point number:", num4)

results = [
    num1 + num2,
    num1 - num2,
    num1 * num2,
    num1 / num2,
    num1 ** num2,
    num1 // num2,
    num1 % num2
]

print("Results of arithmetic operations:", results)

