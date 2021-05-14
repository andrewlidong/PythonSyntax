'''
11. Determine if the number is valid

Given an input string, determine if it makes a valid number or not. For simplicity, assume that white spaces are not present in the input.

4.325 is a valid number.

1.1.1 is NOT a valid number.

222 is a valid number.

is NOT a valid number.
0.1 is a valid number.

22.22. is NOT a valid number.

Solution:

To check if a number is valid, we’ll use the state machine below. The initial state is start, and we’ll process each character to identify the next state. If the state ever ends up at unknown or in a decimal, the number is not valid.

Time: O(N)
Space: O(1)

'''


class STATE:
    START, INTEGER, DECIMAL, UNKNOWN, AFTER_DECIMAL = range(5)


def get_next_state(current_state, ch):
    if (current_state is STATE.START or
            current_state is STATE.INTEGER):
        if ch is '.':
            return STATE.DECIMAL
        elif ch >= '0' and ch <= '9':
            return STATE.INTEGER
        else:
            return STATE.UNKNOWN

    if current_state is STATE.DECIMAL:
        if ch >= '0' and ch <= '9':
            return STATE.AFTER_DECIMAL
        else:
            return STATE.UNKNOWN

    if current_state is STATE.AFTER_DECIMAL:
        if ch >= '0' and ch <= '9':
            return STATE.AFTER_DECIMAL
        else:
            return STATE.UNKNOWN
    return STATE.UNKNOWN


def is_number_valid(s):
    if not s:
        return True

    i = 0
    if s[i] is '+' or s[i] is '-':
        i = i + 1

    current_state = STATE.START

    for c in s[i:]:
        current_state = get_next_state(current_state, c)
        if current_state is STATE.UNKNOWN:
            return False
        i = i + 1

    if current_state is STATE.DECIMAL:
        return False

    return True


print("Is the number valid 4.325? ", is_number_valid("4.325"))
print("Is the number valid 1.1.1? ", is_number_valid("1.1.1"))
print("Is the number valid 222? ", is_number_valid("222"))
print("Is the number valid 22.? ", is_number_valid("22."))
print("Is the number valid 0.1? ", is_number_valid("0.1"))
print("Is the number valid 22.22.? ", is_number_valid("22.22."))
print("Is the number valid 1.? ", is_number_valid("1."))
