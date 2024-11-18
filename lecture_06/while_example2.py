
number = int(input("Enter a non-zero number to square: "))

while number != 0:   # while the number is non-zero
    print(f"The square of {number} is {number * number}")
    number = int(input("Enter another non-zero number to square: "))

print("--- The End ---")