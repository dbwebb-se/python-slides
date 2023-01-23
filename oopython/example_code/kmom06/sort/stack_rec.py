class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return "Empty list."

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def print_bottom_to_top(stack):
    #basfall
    if stack.is_empty():
        return
    #gör något
    top_el = stack.pop()
    #anropa sig själv
    print_bottom_to_top(stack)
    print(top_el) 
    stack.push(top_el)
    return "" # Returns None if no return statement

my_stack = Stack()
my_stack.push("green")
my_stack.push("blue")
my_stack.push("red")

print(print_bottom_to_top(my_stack))

    #stack.push(top_el)