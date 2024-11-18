# 1. for each loop
#    iterables like str, list, dict, range

text = "Hello World!"   # str
for char in text:
    print(char)

print()

# list
names = ["vi", "jinx", "caitlyn", "jayce", "mel medarda", "vander"]
for name in names:
    print(name.title())

print()
# 2. for in range loop
# range(start(opt), end(comp), step(opt))
for i in range(5):   # 0, 1, 2, 3, 4 [start=0, end=5<excluded>]
    print(i)

print()
for i in range(3, 8):  # 3, 4, 5, 6, 7 [start=3, end=8(excluded)]
    print(i)

print()
for i in range(-5, 50, 5): # -5, 0, 5, 10, 15 ... 45
    print(i)   # start = -5, end = 50 (excluded), step = +5

print()
for i in range(10, 0, -1):
    print(i)
print("--- Blast off! ---")

print()
print(*range(10))

print()
for i in range(0, 30+1, 3):
    print(i, end=" ")




