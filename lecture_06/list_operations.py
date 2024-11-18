
numbers = [55, 66, 77, 33, 22, 101, 44, 17, 89, 50]

# add an element to the end of the list
numbers.append(999)
print(numbers)

# remove the element from the end of the list
numbers.pop()
print(numbers)

# insert an element to index 2 of the list
numbers.insert(2, 888)
print(numbers)

# remove the element from position 5
numbers.pop(5)
print(numbers)

number = int(input("Find a number: "))
if number in numbers:
    print(f"{number} is found in the list.")
else:
    print(f"{number} is not found.")

numbers.reverse()    # reverse the order of the list.
print(numbers)

numbers.sort()   # sort in ascending order
print(numbers)

numbers.sort(reverse=True)   # sort in descending order.
print(numbers)