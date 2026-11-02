class MinStack:
    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to store the minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the popped element is the current minimum, pop it from min_stack too
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
