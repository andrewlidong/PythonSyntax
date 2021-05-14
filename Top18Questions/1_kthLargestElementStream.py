'''
1. Find the kth largest element in a number stream

Design a class to efficiently find the Kth largest element in a stream of numbers. The class should have the following two things:​

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer K.

The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Example: 

Input: [4, 1, 3, 12, 7, 14], K = 3
1. Calling add(6) should return '7'.
2. Calling add(13) should return '12'.
2. Calling add(4) should still return '12'.

SOLUTION: 

To solve this problem, we will follow the common Top ‘K’ Elements pattern. So, we want to use a min-heap instead of a max-heap, which would be used for Kth smallest number. As we know, the root is the smallest element in the min heap. So, we can compare every number with root as we iterate through each number. If the number is bigger than root, we will swap the two. We will repeat this process until we have iterated through ever number.

Time: O(log(K))
Space: O(K)
'''

from heapq import *


class KthLargestNumberInStream:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        # add the numbers in the min heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min heap
        heappush(self.minHeap, num)

        # if the heap has more than 'k' numbers, remove one number
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        # return the Kth largest number
        return self.minHeap[0]
