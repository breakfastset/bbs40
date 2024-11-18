
pies = ["shepherd", "apple", "pineapple", "raspberry", "blueberry", "chicken", "taro"]
#         0           1          2          3             4             5         6
#        -7           -6         -5        -4            -3             -2        -1

print(pies[0])  #  shepherd
print(pies[6])  #  taro
print(pies[-1]) #  taro

# list_name[start:end:step]  -> end is excluded
print(pies[1:5])    # apple, pineapple, raspberry, blueberry (excludes chicken)
print(pies[:3])     # shepherd, apple, pineapple  (start=0)
print(pies[4:])     # blueberry, chicken, taro

print(pies[1:6:2])  # apple, raspberry, chicken  (step = 2)
print(pies[::-1])   # print reverse
print(pies[:1:-1])   # ['taro', 'chicken', 'blueberry', 'raspberry', 'pineapple']

pies[3] = "mud"
print(pies)

print("-=" * 40)
pies_2 = pies[:]    # make a copy of pies (new copy)
pies_3 = pies       # pies_3 is pointing to same list as pies
print(pies_2)
print(pies_3)

pies_2[0] = "chocolate"    # affects pie_2 only
pies_3[-1] = "bamboo"      # affects pies and pies_3
print("-=" * 40)
print("-- After modification --")
print(f"pies_2: {pies_2}")   # pies_2 is a different list.
print(f"pies_3: {pies_3}")   # pies_3 and pies are the same list.
print(f"pies  : {pies}")

print(f"Number of pies in pies_2: {len(pies_2)}")
print(pies_2[6])   # indexes go from 0 to len(pies_2) - 1 [ie. 0 to 6]