from basic.Stack import Stack


class ExtendedStack:
    def __init__(self):
        self.stack = Stack()
        self.maxStack = Stack()
        self.maxElement = None
        return

    def push(self, element):
        a = self.maxElement

        if self.maxElement is None:
            self.maxElement = element
            self.stack.push(element)
            return

        if self.maxElement <= element:
            self.maxStack.push(self.maxElement)
            self.maxElement = element
            self.stack.push(element)
            return

        self.stack.push(element)
        return

    def pop(self):
        popedElement = self.stack.pop()

        if self.stack.isEmpty():
            self.maxElement = None
            return popedElement

        if popedElement == self.maxElement:
            self.maxElement = self.maxStack.pop()

        return popedElement

    def max(self):
        return self.maxElement


def executeCommand(s, stack):
    command = s.split(" ")

    if len(command) == 2:
        stack.push(int(command[1]))
    elif command[0] == "pop":
        stack.pop()
    elif command[0] == "max":
        print(stack.max())

    return


stack = ExtendedStack()

n = int(input(""))
arrCommands = []

for i in range(n):
    arrCommands.append(input(""))

for command in arrCommands:
    executeCommand(command, stack)
