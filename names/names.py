import time


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        # if new nodes value is less than go left
        if value < self.value:
            # insert value if no child there
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # if child, repeat process till no child
                self.left.insert(value)
        # if new nodes value is greater than go right
        if value > self.value:
            if not self.right:
                # insert value if no child there
                self.right = BinarySearchTree(value)
            else:
                # if child, repeat process till no child
                self.right.insert(value)


    def contains(self, target):
        # searching a key
        # to search a given key in a binary search tree, we first compare it with root
        # if the key is present at root, return root.
        # if key is greater than root, recur for right subtree of root node
        # else recur for left subtree
        # base case, will return true once done
        if self.value == target:
            return True
        # decide if we are going left or right
        if target < self.value:
            if not self.left:
                return False
            else:
                # use recursion
                return self.left.contains(target)
        else:
            # handle the right side
            if not self.right:
                return False
            else:
                return self.right.contains(target)


    def get_max(self):
        # keep going right until you find a node without a child to the right
        if not self.right:
            return self.value
        else:
            # if there is something on the right, keep going
            return self.right.get_max()


    def for_each(self, callback):
        # we need to traverse the tree similar to how print works in the demo
        # call the function that is passed as an argument, using the value in current node
        callback(self.value)
        if self.left:
            # if left node, call the function on left node, using recursion
            self.left.for_each(callback)
        if self.right:
            self.right.for_each(callback)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

bst = BinarySearchTree("value")
duplicates = []

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_1)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# original runtime 10 seconds
# optimized runtime .23 seconds
