'''
10. Largest sum subarray
In the array below, the largest sum subarray starts at index 3 and ends at 6, and with the largest sum being 12.

Example

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

We will solve this problem by implementing Kadane’s algorithm. The algorithm works by scanning an entire array and at each position find the maximum sum of the subarray ending there. This is achieved by keeping a current_max for the current array index and a global_max. The algorithm is as follows:

current_max = A[0]
global_max = A[0]
for i = 1 -> size of A
    if current_max is less than 0
        then current_max = A[i]
    otherwise 
        current_max = current_max + A[i]
    if global_max is less than current_max 
        then global_max = current_max

Time: O(NK)
Space: O(1)

'''


def max_sub_array_of_size_k(k, arr):
    max_sum, cur_sum = 0, 0

    for i in range(len(arr) - k + 1):
        cur_sum = 0
        for j in range(i, i + k):
            cur_sum += arr[j]
        max_sum = max(max_sum, cur_sum)
    return max_sum
