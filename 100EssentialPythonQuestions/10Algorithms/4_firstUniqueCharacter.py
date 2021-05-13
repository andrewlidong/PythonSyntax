# Given a string, find the first non-repeating character in it and return its index.  If it doesn't exist, return -1.  Note: all the input strings are already lowercase.

# Approach 1
import collections
# deque (list-like container with fast appends and pops on either end)
# Counter (dict subclass for counting hashable objects)
# OrderedDict (dict subclass that remembers the order entries were added)
# defaultdict (dict subclass that calls a factory function to supply missing values)
# https://docs.python.org/3/library/collections.html


def solution(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

print('###')

# Approach 2


def solution(s):
    # build hash map: character and how often it appears
    # gives back a dictionary with words occurrence count
    #Counter({'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1})
    counter = collections.Counter(s)
    # find the index
    # enumerate(iterable, start=0)
    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx
    return -1


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))

# Also in this case, two potential solutions are provided and I guess that, if you are pretty new to algorithms, the first approach looks a bit more familiar as it builds as simple counter starting from an empty dictionary.
# However understanding the second approach will help you much more in the longer term and this is because in this algorithm I simply used collection.Counter(s)instead of building a chars counter myself and replaced range(len(s)) with enumerate(s), a function that can help you identify the index more elegantly.
