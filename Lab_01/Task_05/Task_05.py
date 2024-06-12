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

print("Number of elements in the list:", len(results))

print("Even elements of the list:")
for result in results:
    if result % 2 == 0:
        print(result)

results[1], results[4] = results[4], results[1]

print("Modified list after swapping:")
print(results)

name = input("Enter your surname and name: ")

print("Executor of this laboratory work:", name)

print("This lab exercise illustrates the utilization of Python's input function,")
print("arithmetic operations")
print("and basic string handling.")

