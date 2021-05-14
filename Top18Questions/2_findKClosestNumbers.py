'''
2. Find k closest numbers

Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: [2, 4, 5, 6, 9], k = 3, x = 6
Output: [4, 5, 6]

Once again this problem follows the Top ‘K’ Numbers pattern. Here is our approach to the problem:

Since the array is already sorted, we can first find the number closest to X through binary search. Let’s say that number is Y.
The K closest numbers to K adjacent to Y in the array. We can search both sides of Y to find the closest numbers.
Then, we can use a heap to efficiently search for the closest numbers. We can take K numbers in both directions of Y and push them in a min-heap sorted by their difference from X.
Finally, we extract the top K numbers from the min-heap to find the required numbers.

Time: O(K)
Space: O(log(n - k))
'''
