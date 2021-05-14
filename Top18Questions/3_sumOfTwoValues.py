'''
3. Sum of two values

Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value. Return true if the sum exists and return false if it does not.

Example: 

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

SOLUTION

In this solution, you can use the following algorithm to find a pair that add up to the target (say val).

Scan the whole array once and store visited elements in a hash set. During scan, for every element e in the array, we check if val - e is present in the hash set i.e. val - e is already visited.
If val - e is found in the hash set, it means there is a pair (e, val - e) in array whose sum is equal to the given val.
If we have exhausted all elements in the array and didn’t find any such pair, the function will return false.

# Time: O(N)
# Space: O(N)
'''


def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            return True

        found_values.add(a)

    return False


v = [5, 7, 1, 2, 8, 4, 3]
test = [3, 20, 1, 2, 7]

for i in range(len(test)):
    output = find_sum_of_two(v, test[i])
    print("find_sum_of_two(v, " + str(test[i]) + ") =" + str(output))
