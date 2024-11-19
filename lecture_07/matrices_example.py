seatings = [
    ["James", "April", "Josh"],
    ["Vi", "Powder", "Ekko"],
    ["Yasuo", "Sett", "Jhin"],
    ["Mel", "Viktor", "Yone"]
]

print(seatings[3][1])   # 4th row, 2nd column -> Viktor

print(seatings[1][2])   # 2nd row, 3rd column -> Ekko

print(seatings[2])      # 3rd row ["Yasuo", "Sett", "Jhin"]
print()

for row in range(len(seatings)):    # row in range(4)
    for col in range(len(seatings[row])):    # col in range(3)
        print(seatings[row][col])

# print(seatings[0][0])
# print(seatings[0][1])
# print(seatings[0][2])

# print(seatings[1][0])
# print(seatings[1][1])
# print(seatings[1][2])

# print(seatings[2][0])
# print(seatings[2][1])
# print(seatings[2][2])

# print(seatings[3][0])
# print(seatings[3][1])
# print(seatings[3][2])

print("-" * 50)
print()
print()

print("=" * 40 )
for row in range(len(seatings)):    # row in range(4)
    # start of row
    for col in range(len(seatings[row])):    # col in range(3)
        print(f"{seatings[row][col]:10}", end=" ")
    print()   # print a separator between the rows
    # end of row

print("=" * 40 )




