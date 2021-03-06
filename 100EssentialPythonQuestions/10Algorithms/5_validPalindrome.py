# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'


def solution(s):
    for i in range(len(s)):
        # Lst[Initial: End: IndexJump]
        t = s[:i] + s[i + 1:]
        if t == t[::-1] return True

    return s == s[::-1]


solution(s)

# The “Valid Palindrome” problem is a real classic and you will probably find it repeatedly under many different flavors. In this case, the task is to check weather by removing at most one character, the string matches with its reversed counterpart. When s = ‘radkar’ the function returns Trueas by excluding the ‘k’ we obtain the word ‘radar’ that is a palindrome.
