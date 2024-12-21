# https://www.hackerrank.com/challenges/30-binary-trees
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = []
        index = 0
        q.append(root)
        while index < len(q):
            top = q[index]
            index += 1
            print(top.data, end = " ")
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

