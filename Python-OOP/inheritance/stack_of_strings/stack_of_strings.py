class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)

    def pop(self):
        last_element = self.data.pop()
        return last_element

    def top(self):
        top_element = self.data[-1]
        return top_element

    def is_empty(self):
        if self.data:
            return False
        else:
            return True

    def __str__(self):
        return_list = self.data[::-1]
        return f'[{", ".join(return_list)}]'


books = Stack()

books.push("Jungle Book")
books.push("Djumanji")
books.push(3)
books.push("Mort")
print(books.pop())
print(books.top())


print(books)
