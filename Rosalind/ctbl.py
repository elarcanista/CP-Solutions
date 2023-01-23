class Node:
    nodes = []
    named = {}
    def __init__(self):
        self.name = None
        self.parent = None
        self.visited = False
        self.children = set()
        self.degree = 0
        Node.nodes.append(self)

    def add(self, child):
        self.children.add(child)
        self.degree += 1
        child.degree += 1
        child.parent = self

    def __repr__(self):
        repr = ""
        if len(self.children) > 0:
            repr += "(" + ",".join(map(str, self.children)) + ")"
        if self.name != None:
            repr += self.name
        return repr

def tokenize(A):
    tokens = []
    i = 0
    while i < len(A):
        if A[i] in ["(", ")", ","]:
            tokens.append(A[i])
        elif A[i] not in [";"]:
            name = A[i]
            while A[i+1] not in ["(", ")", ",", ";"]:
                name += A[i+1]
                i += 1
            tokens.append(name)
        i += 1
    tokens.append(";")
    return tokens

def parse(A):
    tokens = tokenize(A)
    stack = [Node()]
    i = 0
    while i < len(tokens):
        if tokens[i] == "(":
            new = Node()
            stack[-1].add(new)
            stack.append(new)
        elif tokens[i] == ")":
            if tokens[i+1].replace("_", "").isalpha():
                stack[-1].name = tokens[i+1]
                i += 1
            stack.pop()
        elif tokens[i] == ";":
            return stack.pop()
        elif tokens[i] == ",":
            pass
        else:
            new = Node()
            new.name = tokens[i]
            stack[-1].add(new)
        i += 1

def BFS(u):
    u.visited = True
    for v in u.children:
        BFS(v)

def get_str():
    ans = ""
    for u in sorted(Node.named.keys()):
        if Node.named[u].visited:
            ans += "1"
        else:
            ans += "0"
    return ans

def reset():
    for u in Node.nodes:
        u.visited = False

parse(input())
Node.nodes = Node.nodes[1:]
Node.nodes[0].parent = None
Node.nodes[0].degree -= 1
for u in Node.nodes:
    if u.name != None:
        Node.named[u.name] = u

ans = []
for u in Node.nodes:
    for v in u.children:
        if len(v.children) == 0:
            continue
        BFS(v)
        ans.append(get_str())
        reset()
for a in sorted(ans):
    print(a)