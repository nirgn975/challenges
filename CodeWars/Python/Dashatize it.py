"""
Given a number, return a string with dash `'-'` marks before and after each odd integer, but do not begin or end the string with a dash mark.
"""

def dashatize(num):
    if not num and not (num == 0):
        return 'None'

    result = '-'.join(str(abs(num)))
    copy_result = result[:]
    occurrences = 0

    for index, value in enumerate(result):
        if value == '-':
            # Check if there is need to be a '-' here.
            if int(result[index - 1]) % 2 == 0 and int(result[index + 1]) % 2 == 0:
                copy_result = copy_result[:index - occurrences] + copy_result[index + 1 - occurrences:]
                occurrences += 1

    return copy_result
