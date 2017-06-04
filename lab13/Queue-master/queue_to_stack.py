from arrayqueue import ArrayQueue
from arraystack import ArrayStack


def queue_to_stack(queue):
    """
    Converts the queue to a stack.
    """
    stk_ar = ArrayStack()
    q = ArrayQueue(queue)
    el = []
    while not q.isEmpty():
        el.append(q.pop())
    q1 = ArrayQueue(el[::-1])
    while not q1.isEmpty():
        stk_ar.push(q1.pop())
    return stk_ar
