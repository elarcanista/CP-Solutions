import sys

class node:
    def __init__(self, name="", children = None):
        self.parent = None
        self.visited = False
        self.name = name
        if children is None:
            self.children = []
        else:
            self.children = children

    def __repr__(self):
        if len(self.children) == 0:
            return self.name
        ans = "("
        ans += ",".join(map(repr, self.children))
        ans += ")" + self.name
        return ans
    
    def add(self, child):
        child.parent = self
        self.children.append(child)

def tokenize(line):
    tokens = []
    curr = ""
    for c in line:
        if c in ["(", ",", ")", ";"]:
            if curr != "":
                tokens.append(curr)
                curr = ""
            if c in ["(", ")", ";"]:
                tokens.append(c)
            else:
                tokens.append("")
        elif c != " ":
            curr += c        
    return tokens

def parse(tokens):
    stack = [node()]
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == "(":
            new = node()
            stack[-1].add(new)
            stack.append(new)
        elif t == ")":
            if tokens[i+1] not in ["(", ")", ";"]:
                stack[-1].name = tokens[i+1]
                i += 1
                if stack[-1].name in query_name:
                    query.append(stack[-1])
            stack.pop()
        elif t != ";":
            stack[-1].add(node(t))
            if t in query_name:
                query.append(stack[-1].children[-1])
        i += 1
    return stack.pop().children[0]

def lca(A, B):
    while A != None:
        A.visited = True
        A = A.parent
    while B.visited == False:
        B = B.parent
    return B

def dist(A,B,C):
    ans = 0
    while A != C:
        A = A.parent
        ans += 1
    while B != C:
        B = B.parent
        ans += 1
    return ans

for i, line in enumerate(sys.stdin):
    if i % 3 == 0:
        test = line.strip()
    if i % 3 == 1:
        query_name = line.strip().split()
        query = []
        parse(tokenize(test))
        C = lca(*query)
        print(dist(*query, C), end=" ")