# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'


def solution(sentence1, sentence2):
    set1 = set(sentence1.split())
    set2 = set(sentence2.split())

    # ^ A.symmetric_difference(B)
    # & A.intersection(B)
    return sorted(list(set1 ^ set2)), sorted(list(set1 & set2))


print(solution(sentence1, sentence2))

# The problem is fairly intuitive but the algorithm takes advantage of a few very common set operations like set(), intersection() or & and symmetric_difference() or ^that are extremely useful to make your solution more elegant. If it is the first time you encounter them, make sure to check this article:
