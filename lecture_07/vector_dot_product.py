def dot_product(vector1, vector2):
    """Return the dot product of 2 equal sized vectors."""
    total = 0.0

    for i in range(len(vector1)):  # for i in range (3), i = 0, 1, 2
        current_result = vector1[i] * vector2[i]   # c_r = v1[2] * v2[2] -> 0.4 * 0.6
        total = total + current_result   # total = 0.06 + 0.24 = 0.3

    return total


def main():
    """Start of Program."""
    v1 = [0.3, 0.0, 0.4]
    #      0    1    2
    v2 = [0.2, 0.5, 0.6]
    result = dot_product(v1, v2)
    print(result)

main()