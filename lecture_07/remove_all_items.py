
items = ["apple", "pear", "orange", "durian", "mangosteen",
         "starfruit", "lemon", "dragonfruit", "pineapple",
         "papaya", "pineapple", "papaya", "lemon", "pineapple"]

# items = list(set(items))
# convert to set to make items unique, convert back to list

target = "pineapple"
while target in items:
    items.remove(target)

print(items)

numbers = [1.0, 2.0, 3.0, 4.0]
numbers *= 3
print(numbers)  # [1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0]

scores = [65, 75, 89, 90, 34, 45, 20, 66, 77, 88, 50]
average_score = sum(scores) / len(scores)
print(f"Avg score: {average_score:.1f}")
max_score = max(scores)
min_score = min(scores)
print(f"Max: {max_score}, Min: {min_score}")