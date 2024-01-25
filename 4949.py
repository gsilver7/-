def is_balanced(string):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return "no"
    return "yes" if not stack else "no"

while True:
    input_str = input()
    if input_str == ".":
        break
    print(is_balanced(input_str))
