# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            Bracket = (next,[next,i+1])
            opening_brackets_stack.append(Bracket)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i+1

            else:
                t = opening_brackets_stack.pop()
                if (t[0][0] == '[' and next != ']') or (t[0][0]== '(' and next != ')') or (t[0][0]== '{' and next != '}'):
                    return i+1
                else:
                    pass
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        if len(opening_brackets_stack) == 1 and i == 0:
            return i+1
        elif i > 0:
            z = opening_brackets_stack[0][1][1]
            return z
        else:
            return False

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
