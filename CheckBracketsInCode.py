from basic.Stack import Stack


def CheckCode(code):
    code = code
    stack = Stack()

    for i in range(len(code)):
        c = code[i]

        if code[i] in ["[", "(", "{"]:
            stack.push((c, i))

        if c in ["]", ")", "}"]:
            if stack.isEmpty():
                return i + 1

            popedElement, index = stack.pop()

            if popedElement + c not in ["[]", "()", "{}"]:
                return i + 1

    if not stack.isEmpty():
        return stack.pop()[1] + 1

    return "Success"


S = input("")
print(CheckCode(S))
