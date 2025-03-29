'''
Homework
'''

'''
1. Reverse a word.
Write a function that takes a string as input and returns the string reversed.

Example 1:
Input: "hello"
Output: "olleh"

Example 2:
Input: "world"
Output: "dlrow"
'''
def reverse_word(word):
    word_arrangement =""
    for character in word:
        word_arrangement = character + word_arrangement
    return word_arrangement




# Test cases
#print(reverse_word("hello"))  # "olleh"
#print(reverse_word("world"))  # "dlrow"
#print(reverse_word("python"))  # "nohtyp"
#print(reverse_word("racecar"))  # "racecar"

'''
2. Sum of borders of 2D list
Given a 2D list of integers, return the sum of the borders.
Example 1:
Input: [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
Output: 40
Explanation: 1 + 2 + 3 + 4 + 6 + 7 + 8 + 9 = 40

Example 2:
Input: [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]
Output: 65
Explanation: 1 + 2 + 3 + 4 + 6 + 7 + 9 + 10 + 11 + 12 = 65

Example 3:
Input: [[1, 2],
        [3, 4],
        [5, 6],
        [7, 8]]
Output: 36
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
'''

def sum_of_borders(nums):
    total=0
    for rows in range(len(nums)):
        for col in range(len(nums[rows])):
            if rows == 0 or rows == len(nums) - 1 or col == 0 or col == len(nums[rows])-1:
                total= total +nums[rows][col]
    return total

# Test cases
print(sum_of_borders([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]))  # Output: 40

print(sum_of_borders([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [10, 11, 12]]))  # Output: 65