import sys
import re

class Node:
    named = {}

    def __init__(self):
        self.children = set()
        self.name = None
        self.parent = None
        self.visited = False
        self.weight = 0

    def add(self, child):
        self.children.add(child)
        child.parent = self

    def set_name(self, name):
        self.name = name
        Node.named[name] = self

    def set_weight(self, weight):
        self.weight = int(weight)
    
    def __repr__(self):
        ans = ""
        if len(self.children) > 0:
            ans += "(" + ",".join([str(a) for a in self.children]) + ")"
        if self.name != None:
            ans += self.name
        if self.parent != None:
            ans += ":" + str(self.weight)
        return ans

def tokenize(A):
    tokens = []
    i = 0
    while i < len(A):
        if A[i] in ["(", ")"]:
            tokens.append(A[i])
        elif A[i] == ":":
            weight = ""
            while A[i+1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                weight += A[i+1]
                i += 1
            tokens.append(weight)
        elif A[i] not in [",", ";"]:
            name = A[i]
            while A[i+1] not in ["(", ")", ",", ":", ";"]:
                name += A[i+1]
                i += 1
            tokens.append(name)
        i += 1
    return tokens + [";"]
    
def parse(A):
    stack = [Node()]
    tokens = tokenize(A)
    i = 0
    while i < len(tokens) - 1:
        if tokens[i] == "(":
            new = Node()
            stack[-1].add(new)
            stack.append(new)
        elif tokens[i] == ")":
            if tokens[i+1].replace('_', '').isalpha():
                stack[-1].set_name(tokens[i+1])
                i += 1
            if tokens[i+1].isnumeric():
                stack[-1].set_weight(tokens[i+1])
                i += 1
            stack.pop()
        else:
            new = Node()
            stack[-1].add(new)
            if tokens[i].replace('_', '').isalpha():
                new.set_name(tokens[i])
                i += 1
            if tokens[i].isnumeric():
                new.set_weight(tokens[i])
        i += 1
    return stack.pop()

def lca(A, B):
    while A != None:
        A.visited = True
        A = A.parent
    while not B.visited:
        B = B.parent
    return B

def dist(A, C):
    ans = 0
    while A != C:
        ans += A.weight
        A = A.parent
    return ans

for i, line in enumerate(sys.stdin):
    if i % 3 == 0:
        root = parse(line.strip())
    elif i % 3 == 1:
        A, B = line.split()
        A = Node.named[A]
        B = Node.named[B]
        C = lca(A, B)
        print(dist(A, C) + dist(B, C), end = " ")
print()