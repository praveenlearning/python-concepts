class Stack:
    def __init__(self):
        self.store = []

    def push(self, ele):
        self.store.append(ele)

    def pop(self):
        return self.store.pop()

    def __str__(self):
        return str(id(self))


if __name__ == '__main__':
    s = Stack()
    print(s)
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    s.push(4)
    print(s)
