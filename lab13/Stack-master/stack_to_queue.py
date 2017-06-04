from arraystack import ArrayStack
from arrayqueue import ArrayQueue

def stack_to_queue(stack):
    """
    Converts the stack to a queue.
    """
    q = ArrayQueue()
    for i in list(stack)[::-1]:
        q.add(i)
    return q
