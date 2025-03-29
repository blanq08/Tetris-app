def sum_of_borders(nums):
    if not nums:  # Check if the list is empty
        return 0

    rows = len(nums)
    cols = len(nums[0])

    total = 0

    for i in range(rows):
        for j in range(cols):
            # Check if the element is on the border
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                total += nums[i][j]

    return total

# Test cases
print(sum_of_borders([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]))  # 40

print(sum_of_borders([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [10, 11, 12]]))  # 65
