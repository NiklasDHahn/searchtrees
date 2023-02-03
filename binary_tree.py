"""
Module containing Binary Tree operations.
"""

# import random

class BinaryTree:
    """
    Class for building and retrieving items from a Binary Tree.
    """

    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


    def add_val(self, data):
        """
        Adds the given value to the BT. Sets it as root if root it None.
        Left child if root is not None and if value is smaller than root.
        Right child if root is not None and if value is greater than root.
        """

        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.add_val(data)
            elif data > self.val:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.add_val(data)
        else:
            self.val = data


    def print_tree(self):
        """
        Print the items in the BT.
        """

        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        print(self.val)

    def tree_level(self):
        """
        Extract the level and total number of nodes of a BT.
        """
        level = 0
        total = 0
        queue = [[self, 0]]
        while len(queue) != 0:
            el = queue.pop(0)
            level = max(level, el[1])
            total += 1

            if el[0].left is not None:
                queue.append([el[0].left, el[1] + 1])
            if el[0].right is not None:
                queue.append([el[0].right, el[1] + 1])

        return level, total
    
    # TODO: Remove item from BT
    # TODO: Search for item in BT



# if __name__ == '__main__':
#     bt = BinaryTree(10)
#     for number in [random.randint(0,1000) for i in range(10)]:
#         bt.add_val(number)
#     # bt.print_tree()
#     print(bt.tree_level())
    