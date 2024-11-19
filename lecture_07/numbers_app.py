
def find_median(numbers):
    """Find median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) % 2 == 0:
        middle_right_index = len(sorted_numbers) // 2
        middle_left_index = middle_right_index - 1
        median_value = (sorted_numbers[middle_left_index] + sorted_numbers[middle_right_index]) / 2
    else:
        middle_index = len(sorted_numbers) // 2
        median_value = sorted_numbers[middle_index]
    return median_value

def main():
    """Start of program."""
    scores = [65, 75, 89, 90, 34, 45, 20, 66, 77, 88, 50]
    median = find_median(scores)
    print(f"Median: {median}")

main()