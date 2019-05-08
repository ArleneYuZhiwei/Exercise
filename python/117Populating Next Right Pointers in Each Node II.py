"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#BFS:
#if there more than one nodes in the same level, the left one will point the right one
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        tmpnodes=[root]
        while len(tmpnodes)>0:
            for i in range(0,len(tmpnodes)-1):
                tmpnodes[i].next=tmpnodes[i+1]
            nextnodes=[]
            for n in tmpnodes:
                if n.left is not None:
                    nextnodes.append(n.left)
                if n.right is not None:
                    nextnodes.append(n.right)
            tmpnodes=nextnodes
        return root

#dequeue is faster 
class Solution(object):  
    def connect(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root
        self.head = root
        q = deque()
        q.append(root)
        q.append(None)
        upnode = None
        while q:
            tmp = q.popleft()
            if not tmp:
                if q:
                    q.append(None)
                upnode = None
            else:
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
                if  upnode:
                    upnode.next = tmp
                upnode = tmp
        return self.head
#use two point to record the data space O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root        
        left_most = root
        while left_most:
            cur = left_most
            pre, left_most = None, None
            while cur:
                if cur.left:
                    left_most = cur.left
                    break
                if cur.right:
                    left_most = cur.right
                    break
                cur = cur.next
            pre = None
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    pre = cur.left
                
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    pre = cur.right               
                cur = cur.next        
        return root