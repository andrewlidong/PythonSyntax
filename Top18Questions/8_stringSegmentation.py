'''
8. String segmentation
You are given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary. The following two examples elaborate on the problem further.

Example

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

This problem can be tackled by segmenting the input strign at every possible index to see if the string can be completely segmented into words in the dictionary. We can use an algorithm as follows:

n = length of input string
for i = 0 to n - 1
  first_word = substring (input string from index [0, i] )
  second_word = substring (input string from index [i + 1, n - 1] )
  if dictionary has first_word
    if second_word is in dictionary OR second_word is of zero length, then return true
    recursively call this method with second_word as input and return true if it can be segmented

Time: O(2^N) without memoization
Space: O(N^2)
'''


def can_segment_string(s, dictionary):
    #TODO: Write - Your - Code
    return False
