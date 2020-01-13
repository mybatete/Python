from Stack import Stack
from Queue2 import Queue2

def main():
    stack = Stack()
    for num in xrange(10):
        stack.push(num)
    result = Stack2Queue(stack)
    result.traversal()


def Stack2Queue(stack):
    result = Queue2()
    transition  = Stack()
    while stack.isEmpty() != True:
        c = stack.pop()
        transition.push(c)

    while transition.isEmpty() !=True:
        c = transition.pop()
        result.enqueue(c)

    return result
main()
