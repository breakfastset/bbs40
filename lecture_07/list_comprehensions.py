
# normal loop, no list comprehensions
odd_numbers = []
for i in range(10):
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)

odd_numbers2 = [x for x in range(10) if x % 2 == 1]
print(odd_numbers2)

print("===" * 30)

numbers = [x for x in range(5)]   # 0, 1, 2, 3, 4
print(numbers)

even_numbers = [x for x in range(5) if x % 2 == 0]   # 0, 2, 4
print(even_numbers)

squared_even_numbers = [x ** 2 for x in range(5) if x % 2 == 0]
print(squared_even_numbers)  # [0, 4, 16]

stars = [n * "*" for n in range(5) if n % 2 == 0]
print(stars)   # ['', '**', '****']

scores = [65, 75, 89, 90, 34, 45, 20, 66, 77, 88, 50]
passed_scores = [x for x in scores if x >= 50]
print(passed_scores)

grades = ["passed" if x >= 50 else "failed" for x in scores]
print(grades)

num_passed = len([x for x in scores if x >= 50])
print(f"number of passes: {num_passed}")

num_passed2 = sum([1 if x >= 50 else 0 for x in scores])
print(f"number of passes: {num_passed2}")