
fast_food = ["mcdonalds", "shake shack", "jollibee", "kfc",
             "burger king", "popeyes", "five guys", "wendy's",
             "chipotle", "dominoes", "pizza hut"]

# for each loop -> read-only loop
for food in fast_food:
    if len(food) > 7:
        print(food.title())
    food = food.upper()  # attempt to change to uppercase for each food

print(fast_food)  # original list is unchanged.
# food in for loop is a local variable

# for in range() loop -> for modification
for i in range(len(fast_food)):  # i = 0, 1, 2 ... 10
    if fast_food[i].startswith("p"):    # if current item (string) starts with "p"
        fast_food[i] = fast_food[i].upper()   # modify current item to upper case.

print(fast_food)  # original list is now modified.
