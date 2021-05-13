# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

n = 35


def solution(n):
    prime_nums = []
    # for loop with range
    for num in range(n):
        if num > 1:  # all prime numbers are greater than 1
            # range(start, stop, step)
            for i in range(2, num):
                # if the modulus == 0 it means that the number can be divided by a number preceding it
                if (num % i) == 0:
                    # break terminates the current loop and resumes execution at the next statement.
                    # continue returns the control to the beginning of the while loop
                    break
                else:
                    prime_nums.append(num)
    return prime_nums


solution(n)

# I wanted to close this section with another classic problem. A solution can be found pretty easily looping trough range(n) if you are familiar with both the prime numbers definition and the modulus operation.
