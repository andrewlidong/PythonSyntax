'''
9. Find all palindrome substrings
Given a string find all substrings that are palindromes. For instance:

Example

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Solution

We will iterate through each letter in the input string. For each letter, we can find palindromes by expanding to the left and right will we check for even and odd length palindromes. If there are no palindromes, move to the next letter.

We find palindromes by checking if the left and right character are equal. If they are, we print out the palindrome substring.

Time: O(N^2) without memoization
Space: O(1)
'''


def find_all_palindrome_substrings(input):
    # TODO: Write - Your - Code
    return -1
