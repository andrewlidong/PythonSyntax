'''
17. Find the missing number

We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number. See the example below.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7

Solution:

Here is the algorithm:

Find the sum ‘sum_of_elements’ of all the numbers in the array. This would require a linear scan, O(n).

Then find the sum ‘expected_sum’ of first ‘n’ numbers using the arithmetic series sum formula i.e. ( n * (n + 1) ) / 2.

The difference between these i.e. ‘expected_sum - sum_of_elements’, is the missing number in the array.

Time: O(N)
Space: O(1)
'''


def find_missing(input):
    # calculate sum of all elements in input list
    sum_of_elements = sum(input)

    # there is exactly 1 number missing
    n = len(input) + 1
    actual_sum = (n * (n - 1)) / 2
    return actual_sum - sum_of_elements


def test(n):
    missing_element = random.randint(1, n)
    v = []
    for i in range(1, n):
        if i != missing_element:
            v.append(i)

    actual_missing = find_missing(v)
    print("Expected Missing = ", missing_element,
          " Actual Missing = ", actual_missing)
    assert missing_element == actual_missing


def main():
    for n in range(1, 10):
        test(1000000)


main()
