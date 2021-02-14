import math

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_node(self, root, data):
        if not root:
            node = TreeNode(data)
            self.root = node
        else:
            node = root
            if node.data == data:
                return
            if data < node.data:
                if not node.left:
                    node.left = TreeNode(data)
                else:
                    self.add_node(node.left, data)
            else:
                if not node.right:
                    node.right = TreeNode(data)
                else:
                    self.add_node(node.right, data)

    def print_pre_order(self, root):
        if not root:
            return
        print("{}-->".format(root.data), end='')
        self.print_pre_order(root.left)
        self.print_pre_order(root.right)

    def print_in_order(self, root):
        if not root:
            return
        self.print_in_order(root.left)
        print("{}-->".format(root.data), end='')
        self.print_in_order(root.right)
    
    def print_post_order(self, root):
        if not root:
            return
        self.print_post_order(root.left)
        self.print_post_order(root.right)
        print("{}-->".format(root.data), end='')

    def is_bst(self, root, min, max):
        '''
        Check if tree is a binary search tree
        '''
        if not root:
            return True
        node = root
        if node.data >= min and node.data < max and self.is_bst(node.left, min, node.data) and self.is_bst(node.right, node.data, max):
            return True
        else:
            return False

    def get_height(self, root):
        '''
        returns height or max depth of tree
        '''
        if not root:
            return -1
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def delete_node(self, data):
        pass


if __name__ == '__main__':
    bst = BST()
    bst.add_node(bst.root, 7)
    bst.add_node(bst.root, 4)
    bst.add_node(bst.root, 6)
    bst.add_node(bst.root, 9)
    bst.add_node(bst.root, 1)
    bst.print_post_order(bst.root)
    print('\n{}'.format(bst.is_bst(bst.root, -math.inf, math.inf)))
    print(bst.get_height(bst.root))
