#trees
#manual allocation
class Node:
    def __init__(self,data) -> None:
        self.data=data 
        self.left=None
        self.right=None
'''def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        inorder(root.left)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.data) 
t=Node(1)
a=Node(2)
b=Node(3)
t.left=a
t.right=b
#print(t.right.data)
#print(t.left.data)
inorder(t)
preorder(t)
postorder(t)'''
#binary search tree-application of terrs
class trees:
    def __init__(self):
        self.root=None
    def insert(self,data):
        nn=Node(data)
        if self.root==None:
            self.root=nn
        else:
            curr=self.root
            #infinite loop bcoz we dont konw where to stop
            while True:
                if curr.data<=data:
                    if curr.right==None:
                        curr.right=nn
                        break
                    else:
                        curr=curr.right
                else:
                    if curr.left==None:
                        curr.left=nn
                        break
                    else:
                        curr=curr.left
    def searchnode(self,data):
        s=self.search(self.root,data)
        if s!=None:
            print("found")
        else:
            print("Not")
    def search(self,root,data):
        if root==None or root.data==data:
            return root
        else:
            return self.search(root.left) or self.search(root.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
t=trees()
t.insert(5)
t.insert(6)
t.insert(3)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(2)
t.insert(1)
inorder(t.root)


















if not root1 and not root2:
            return None
        if root1 and root2:
            nn=TreeNode(root1.val+root2.val)
        if root1 or root2:
            if root1:
                nn=TreeNode(root1.val)
            if root2:
                nn=TreeNode(root2.val)
        cur=nn
        def merge(root1,root2,cur):
            if not root1 and not root2:
                return 0
            if root1 and root2:
                cur.val=root1.val+root2.val
            if root1 or root2:
                if root1:
                    return root1.val
                if root2:
                    return root2.val
            l=merge(root1.left,root2.left,cur.left)
            r=merge(root1.right,root2.right,cur.right)
            cur.left=l
            cur.right=r
        merge(root1,root2,cur)
        return nn