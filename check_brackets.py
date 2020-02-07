# python3

import os

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, bracket in enumerate(text):
        if bracket in "([{":
            opening_brackets_stack.append(Bracket(bracket, i))

        if bracket in ")]}":
            if len(opening_brackets_stack) == 0:
                return i
            opening_bracket = opening_brackets_stack[-1].char
            if are_matching(opening_bracket, bracket):
                opening_brackets_stack.pop()
            else:
                return i
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0].position
    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(str(mismatch + 1))


# def test_main():
#     def get_text(path):
#         with open(path) as file:
#             return file.readline()
#
#     directory = "./tests/"
#     for filename in os.listdir(directory):
#         if not filename.endswith(".a"):
#             text = get_text(f"{directory}/{filename}")
#             answer = get_text(f"{directory}/{filename}.a")
#             result = find_mismatch(text)
#             if answer == "Success\n":
#                 assert result == -1
#             else:
#                 assert int(answer) == result + 1
#     print("TEST PASSED")


if __name__ == "__main__":
    main()
