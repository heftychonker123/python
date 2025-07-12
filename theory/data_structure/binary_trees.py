class Node:
    def __init__(self,label):
        self.label=label
        self.left=None
        self.right=None
first_node=Node(1)
second_node=Node(2)
third_node=Node(3)
fourth_node=Node(4)
fifth_node=Node(5)
first_node.left=second_node
first_node.right=third_node
second_node.left=fourth_node
second_node.right=fifth_node
def inorder_traverse(root):
    #if node doesn't exist , return to the prev node
    if root is None:
        return
    #traverse the left node first
    inorder_traverse(root.left)
    #print the data of the node
    print(root.label)
    #traverse the right node
    inorder_traverse(root.right)
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
def postorder_traverse(root):
    #if node doesn't exist , return to the prev node
    if root is None:
        return
    #traverse the left node first
    postorder_traverse(root.left)
    
    #traverse the right node
    postorder_traverse(root.right)
    #print the data of the node
    print(root.label)