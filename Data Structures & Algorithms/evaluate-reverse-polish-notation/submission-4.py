class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        oper = {"+": lambda a,b: a+b,
                 "-": lambda a,b: a-b,
                 "*" :lambda a,b: a*b,
                 "/":lambda a,b: int(a/b)}
        for c in tokens:
            if c not in oper:
                stack.append(c)
            if c in oper:
                a = stack.pop()
                b = stack.pop()
                stack.append(oper[c](int(b), int(a)))
        if len(stack) > 1:
            return 0
        print(stack[0])
        return int(stack[0])

        