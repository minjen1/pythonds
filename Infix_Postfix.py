from pythonds.basic import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    previous_token = None


    for token in tokenList:
        if token.isalnum():
            if previous_token in ('opnd', ')'):
                raise ValueError("Invalid syntax: missing operator before " + token)
            postfixList.append(token)
            previous_token = 'opnd'
            continue

        if token == '(':
            if previous_token in ('opnd', ')'): 
                raise ValueError("Invalid syntax: missing operator before (")
            opStack.push(token)
            previous_token = '('
            continue


        if token == ')':
            if previous_token in (None, 'op', '('): 
                raise ValueError("Right parenthesis missplaced or missing operand before )")
            while not opStack.isEmpty() and opStack.peek() != '(':
                postfixList.append(opStack.pop())
            if opStack.isEmpty():
                raise ValueError("Invalid parentheses")
            opStack.pop()
            previous_token = ')'
            continue

        if token in prec:
            if previous_token in (None, 'op', '('): 
                raise ValueError("Invalid syntax: missing operand before " + token)
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
            previous_token = 'op'
            continue

        if previous_token in (None, 'op', '('):
            raise ValueError("Expression ends unexpectedly " + token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("5 * 3 * ( 4 - 2 )"))
print(infixToPostfix("((5 * 3) * ( 4 - 2 ))*2"))
