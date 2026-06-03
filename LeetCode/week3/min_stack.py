# T: O(1), S: O(n)
class MinStack:
    def __init__(self):
        self.container = []

    def push(self, val: int) -> None:
        if not self.container:
            self.container.append((val, val))
        else:
            current_min = self.container[-1][-1]
            self.container.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.container:
            self.container.pop(-1)

    def top(self) -> int | None:
        if not self.container:
            return None
        return self.container[-1][0]

    def get_min(self) -> int | None:
        if not self.container:
            return None
        return self.container[-1][-1]


obj = MinStack()
obj.push(10)
obj.push(7)
obj.push(3)
obj.push(1)
print(obj.top())
print(obj.get_min())
