# type: ignore (this is added because linter doesn't recognize types that can be both a BST and None)

import priority_queue_tests
import sys

# NOTE: Although there is more than one way to approach this, it's easiest to work
# It is easiest to enforce the following statements at all times:
# - When `value` is None, `left` and `right` are always None.
# - When `value` is not None, `left` and `right` always reference BinarySearchTree objects (that may have None `value`s).
# The validate() methods validate these statements (among other things).


class BinarySearchTree:
    def __init__(self):
        """Create an empty binary search (sub)tree."""
        self.left: None | BinarySearchTree = None
        self.right: None | BinarySearchTree = None
        self.value: None | int = None

    def add(self, value):
        """Add `value` at the correct position to the binary search (sub)tree."""
        if self.is_empty():
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()

        elif value < self.value:
            self.left.add(value)

        elif value > self.value:
            self.right.add(value)
    
    def has(self, value):
        """Returns `True` if the (sub)tree contains `value`, and `False` otherwise."""
        if self.value == None:
            return False
        
        if self.value == value:
            return True

        elif value < self.value:
            return self.left.has(value)

        elif value > self.value:
            return self.right.has(value)

    def is_empty(self):
        """Returns `True` if the (sub)tree is empty, and `False` otherwise."""
        return self.value is None

    def to_list(self) -> list:
        """Returns the (sub)tree as an ordered list of values."""
        result = []

        def traverse(node):
            if node is None or node.value is None:
                return

            traverse(node.left)
            result.append(node.value)
            traverse(node.right)

        traverse(self)

        return result

    def fetch_smallest(self):
        """Finds the smallest value in the (sub)tree, removes it from the tree
        and returns it."""
        if self.left and self.left.value is None:
            value = self.value
            self.remove(value)
            return value

        return self.left.fetch_smallest() if self.left else None

    def remove(self, value):
        """Remove `value` from the (sub)tree. Returns a boolean indicating if
        the value was found."""
        if self.value is None:
            return False
        
        if self.value != value:
            if value > self.value:
                return self.right.remove(value)
            
            elif value < self.value:
                return self.left.remove(value)

        if self.left.is_empty() and self.right.is_empty():
            self.value = None
            self.left = None
            self.right = None
            return True
            
        elif self.left.is_empty():
            child = self.right

        elif self.right.is_empty():
            child = self.left

        else:
            self.value = self.right.fetch_smallest()
            return True

        self.left = child.left
        self.value = child.value
        self.right = child.right
        
        return True

    def validate(self):
        """Validate if the (sub)tree is a consistent binary search tree. Raises
        an exception if a problem is found."""
        result = self.validate_recurse()
        if result:
            self.print()
            result.reverse()
            raise Exception(' ➔ '.join(result))

    def validate_recurse(self):
        """Helper function for validate()."""
        if self.value is None:
            if self.left is not None:
                return ["Empty node should not have children", "left"]
            if self.right is not None:
                return ["Empty node should not have children", "right"]
        else:
            assert self.left and self.right
            if (self.left.value is not None and self.left.value > self.value):
                return ["Left child larger than parent", "left"]
            if (self.right.value is not None and self.right.value < self.value):
                return ["Right child smaller than parent", "right"]
            return self.left.validate_recurse() or self.right.validate_recurse()
        return None

    def print(self, indent=0):
        """Prints the structure of the (sub)tree."""
        pre = ' '*indent + ' ➔'
        if self.value is None:
            print(pre, 'empty')
        else:
            assert self.left and self.right
            self.left.print(indent + 4)
            print(pre, self.value)
            self.right.print(indent + 4)


if __name__ == '__main__':

    def test(*ops):
        print("\n\nTest: ", end="")
        bst = BinarySearchTree()
        assert bst.is_empty()
        expected = []
        for op in ops:
            print(op, end=" ")
            if op > 0:
                bst.add(op)
                expected.append(op)
            else:
                bst.remove(-op)
                expected.remove(-op)
            bst.validate()
            assert bst.is_empty() == (not expected)
        print("")
        bst.print()

        for i in range(20):
            if i in expected and not bst.has(i):
                raise Exception(f"has({i}) returned false")
            if i not in expected and bst.has(i):
                raise Exception(f"has({i}) returned true")

        out = bst.to_list()
        expected.sort()
        if expected != out:
            raise Exception(f"to_list() output ({out}) doesn't match expected expected ({expected})")

    command = sys.argv[1] if len(sys.argv) >= 2 else None

    if command == 'add':
        test(+2, +1, +3)
        test(+5, +2, +6, +1)
        test(+5, +2, +3, +1, +8, +6, +7, +9)

    elif command == 'remove':
        test(+2, +1, +3, -3) # Delete a leaf node
        test(+5, +2, +6, +1, -2) # Delete a node with one child
        test(+5, +4, +3, +2, +1, -4) # Delete a node with one child
        test(+1, +2, +3, +4, +5, -2) # Delete a node with one child
        test(+5, +2, +3, +1, +8, +6, +7, +9, -5) # Delete a node with two children

    elif command == 'unbalanced':
        test(+1, +2, +3, +4, +5, +6, +7, +8, +9, +10, +11, +12, +13) # Create an unbalanced tree

    elif command == 'priority':
        priority_queue_tests.run_all_tests(BinarySearchTree)

    else:
        print(f"Usage: {sys.argv[0]} {{ add | remove | unbalanced | priority }}")
