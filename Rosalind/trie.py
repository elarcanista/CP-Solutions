import sys

def add(root, S):
    for c in S:
        if c in root:
            root = root[c]
        else:
            root[c] = {}
            root = root[c]

def DFS(root, node):
    global node_counter
    for nucleotide, child in root.items():
        node_counter += 1
        print(node, node_counter, nucleotide)
        DFS(child, node_counter)

global node_counter
node_counter = 1
root = {}

for line in sys.stdin:
    add(root, line.strip())
DFS(root, 1)