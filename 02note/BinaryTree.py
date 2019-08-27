# BinaryTree.py

class Node(object):
	"""docstring for Node"""
	def __init__(self, elem,lchild=None,rchild=None):
		super(Node, self).__init__()
		self.elem = elem
		self.lchild=lchild
		self.rchild=rchild



class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, root=None):
		super(BinaryTree, self).__init__()
		self.root = root


	def add(self,elem):
		node=Node(elem)
		# 如果当前的树为空的话，直接将新元素赋值给根节点
		if self.root is None:
			self.root=node
			return
		# 如果不为空，将树放入队列，这里采用广度优先遍历，即弹出一个节点就使其两个子节点入队列
		else:
			queue=[]
			# 根节点入队列，
			queue.append(self.root)
			# 层次遍历，及广度优先遍历
			while queue:
				cur=queue.pop(0)
				if cur.lchild is None:
					cur.lchild = node
					return
				elif cur.rchild is None:
					cur.rchild = node
					return
				else:
					queue.append(cur.lchild)
					queue.append(cur.rchild)


	def breadth_travel(self):
		if self.root is None:
			return	
		queue=[self.root]
		while queue:
			cur=queue.pop(0)
			print(cur.elem,end = ' ')
			if cur.lchild is not None:
				queue.append(cur.lchild)
			# 这里不能用elif 否则在左子节点不为空的情况下就只遍历左子节点而不会进入右子节点了
			if cur.rchild is not None:
				queue.append(cur.rchild)
			


	# 深度遍历:先序遍历.中序遍历.后序遍历:这里的顺序是指根放在什么地方 
	def preorder(self,node):
		if node==None:
			return
		print(node.elem,end = " ")
		self.preorder(node.lchild)
		self.preorder(node.rchild)



	def inorder(self,node):
		if node==None:
			return
		self.inorder(node.lchild)
		print(node.elem,end = " ")
		self.inorder(node.rchild)


	def postorder(self,node):
		if node==None:
			return
		print(node.elem,end = " ")
		self.postorder(node.lchild)
		self.postorder(node.rchild)
		print(node.elem,end = " ")



if __name__ == '__main__':
	bt=BinaryTree()

	bt.add(1)
	bt.add(2)
	bt.add(3)
	bt.add(4)
	bt.add(5)
	bt.add(6)
	bt.add(7)
	bt.add(8)
	bt.add(9)

	bt.breadth_travel()
	print(" ")

	bt.preorder(bt.root)
	print(" ")
	
	bt.inorder(bt.root)
	print("")

	bt.postorder(bt.root)
	print(" ")