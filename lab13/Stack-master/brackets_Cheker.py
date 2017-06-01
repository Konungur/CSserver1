from linkedstack import LinkedStack
def brackets_Checker():
    stk = LinkedStack()
    for ch in exp:
        if ch in ['[', '(']:
            stk.push(ch)
        elif ch in [']', ')']:
            if stk.isEmpty():
                return False
            chFromStack = stk.pop()
            if ch == ']' and chFromStack != '[' or ch == ')' and chFromStack != '(':
                return False
        return stk.isEmpty()
