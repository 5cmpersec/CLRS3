class TreeNode(object):
	def __init__(self, key, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent

	def __str__(self):
		return "({})".format(self.key)

class BST(object):
	def __init__(self, root=None):
		self.root = root

def TreeSearch(root, key):
	if root is None or root.key == key:
		return root

	return TreeSearch(root.left, key) if key < root.key else TreeSearch(root.right, key)

def IterativeTreeSearch(root, key):
	while root is not None and key != root.key:
		root = root.left if key < root.key else root.right
	return root

def TreeMinimum(root):
	while root is not None and root.left is not None:
		root = root.left
	return root

def TreeMaximum(root):
	while root is not None and root.right is not None:
		root = root.right
	return root

def TreeSuccessor(node):
	if node is None:
		return None
	if node.right is not None:
		return TreeMinimum(node.right)
	y = node.parent
	while y is not None and y.right == node:
		node = y
		y = y.parent
	return y


def TreePredecessor(node):
	if node is None:
		return None
	if node.left is not None:
		return TreeMaximum(node.left)
	y = node.parent
	while y is not None and y.left == node:
		node = y
		y = y.parent
	return y

def InorderTreeWalk(root):
	if root is None:
		return
	InorderTreeWalk(root.left)
	print(root.key)
	InorderTreeWalk(root.right)

def TreeInsert(tree, node):
	y = None
	x = tree.root
	while x is not None:
		y = x
		x = x.left if node.key < x.key else x.right
	node.parent = y
	if y is None:
		tree.root = node
	elif node.key < y.key:
		y.left = node
	else:
		y.right = node


if __name__ == '__main__':
	n2 = TreeNode(2)
	n4 = TreeNode(4)
	n3 = TreeNode(3, left=n2, right=n4)
	n2.parent = n3
	n4.parent = n3
	n9 = TreeNode(9)
	n13 = TreeNode(13, left=n9)
	n9.parent = n13
	n7 = TreeNode(7, right=n13)
	n13.parent = n7
	n6 = TreeNode(6, left=n3, right=n7)
	n3.parent = n6
	n7.parent = n6
	n17 = TreeNode(17)
	n20 = TreeNode(20)
	n18 = TreeNode(18, left=n17, right=n20)
	n17.parent = n18
	n20.parent = n18
	root = TreeNode(15, left=n6, right=n18)
	n6.parent = root
	n18.parent = root
	InorderTreeWalk(root)

	print(TreeSuccessor(n6))
	print(TreeSuccessor(n13))
	print(TreePredecessor(n6))
	print(TreePredecessor(n17))
	tree = BST(root)
	TreeInsert(tree, TreeNode(10))
	InorderTreeWalk(tree.root)

