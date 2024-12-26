def parse(text):
    stack = [[]]
    for c in text:
        if c == "(":
            head = []
            stack[-1].append(head)
            stack.append(head)
        elif c == ")":
            if len(stack[-1]) == 3 or stack[-1][-1] == "*":
                stack[-1][0], stack[-1][1] = stack[-1][1], stack[-1][0]
            else:
                stack[-1].insert(0, "c")
            stack.pop()
        else:
            stack[-1].append(c)
    return stack.pop()

for _ in range(int(input())):
    text, length = input().split()
    length = int(length)
    ast = parse(text)
    print(ast)
