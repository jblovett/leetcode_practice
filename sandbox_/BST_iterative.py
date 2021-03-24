

def BST_insert(root, value):
    node = root
    while (1):
        if (node.right):
            node = node.right
            continue
        else:
            node.right = BST()