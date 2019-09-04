# 操作给定的二叉树，将其变换为源二叉树的镜像。
# 输入描述
# 二叉树的镜像定义：源二叉树 
#	 		8
#	 	   /  \
#	 	  6   10
#	 	 / \  / \
#	 	5  7 9 11
#	 	镜像二叉树
#	 		8
#	 	   /  \
#	 	  10   6
#	 	 / \  / \
#	 	11 9 7  5


# 实质上就是每一棵树的左右子树翻转，直接从根节点开始递归交换每一个节点的左右节点的值

from BinaryTree import BinaryTree


# 递归的做法
class Solution():
	# 返回镜像树的根节点
	def Mirror(self, root):
		if root is None:
			return
		else:
			root.lchild,root.rchild=root.rchild,root.lchild
			if root.lchild:
				self.Mirror(root.lchild)
			if root.rchild:
				self.Mirror(root.rchild)
		return 








if __name__ == '__main__':
	bt=BinaryTree()

	# add 广度优先
	bt.add(1)
	bt.add(2)
	bt.add(3)
	bt.add(4)
	bt.add(5)

	bt.preorder(bt.root)
	
	s=Solution()
	s.Mirror(bt.root)
	print("")

	bt.preorder(bt.root)

