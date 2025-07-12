class Node:
    def __init__(self,label):
        self.label=label
        self.left=None
        self.right=None
def insert(root,label):
    if root is None:
        return Node(label)
    if root.label==label:
        return root
    if root.label>label:
        root.left= insert(root.left,label)
    if root.label<label:
        root.right=insert(root.right,label)
    return root
def delete(root, key):
    if not root:
        return None

    if root.label > key:
        root.left = delete(root.left, key)
    elif root.label < key:
        root.right = delete(root.right, key)
    else:
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children: get the inorder successor
        successor = find_min(root.right)
        root.label = successor.label
        root.right = delete(root.right, successor.label)

    return root

def find_min(root):
    while root.left:
        root = root.left
    return root

r=Node(1)
r=insert(r,2)
r=insert(r,4)
r=insert(r,-1)
r=delete(r,2)
def preorder_traverse(root):
    #if node doesn't exist , return to the prev node
    if root is None:
        return
    #print the data of the node
    print(root.label)
    #traverse the left node first
    preorder_traverse(root.left)
    
    #traverse the right node
    preorder_traverse(root.right)
preorder_traverse(r)