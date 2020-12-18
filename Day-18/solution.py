# --- Day 18: Operation Order ---

def infix_to_postfix(expression, priority):
    stack = []
    output = ''

    for ch in expression:
        if ch not in ['+', '*', '(', ')']:
            output += ch
        elif ch == '(':
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[ch] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output


def evaluate(expression, priority):
    postfix = infix_to_postfix(expression, priority)
    stack = []

    for ch in postfix:
        if ch == '+':
            stack.append(stack.pop() + stack.pop())
        elif ch == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(ch))

    return stack.pop()


lines = [line.strip() for line in open('input.txt')]

print("First part: ",
      sum(map(lambda line: evaluate(line.replace(' ', ''), {'+': 1, '*': 1}), lines)))
print("Second part: ",
      sum(map(lambda line: evaluate(line.replace(' ', ''), {'+': 2, '*': 1}), lines)))
