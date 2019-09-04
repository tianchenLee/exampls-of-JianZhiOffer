# HasSubtree.py
#desc 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#solution 判断一棵树是否是另一棵树的子树，可以将两棵树通过某一方法遍历，然后查看B是否A的子集；-- 不可以这样做，因为遍历顺序的问题，有些节点即使不在同一棵书上但也有可能在同一位置出现；

# 本题思路可以是：
# 查找树A中是否有和B的根节点一样的值，
# 若不存在则返回false，
# 若存在则继续遍历并且判断以该节点为根节点的子树是否和B具有相同的结构；
# 参考自本题牛客通过的代码 https://www.nowcoder.com/profile/9326943/codeBookDetail?submissionId=12338565


# -*- coding:utf-8 -*-
class TreeNode:
	 def __init__(self, x):
		 self.val = x
		 self.left = None
		 self.right = None

class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, root=None):
		super(BinaryTree, self).__init__()
		self.root = root


	def add(self,elem):
		node=TreeNode(elem)
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
				if cur.left is None:
					cur.left = node
					return
				elif cur.right is None:
					cur.right = node
					return
				else:
					queue.append(cur.left)
					queue.append(cur.right)



class Solution():
	def HasSubtree(self, pRoot1, pRoot2):
		# write code here
		result = False
		# 若某一棵树为空则返回false
		if pRoot1!=None and pRoot2!=None:
			# 若根节点的值相同则从根节点开始看树A是否包含树B
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree2(pRoot1,pRoot2)
			# 若根节点的值不同则分别递归左右两个节点
			if not result:
				result=self.HasSubtree(pRoot1.left,pRoot2)
			if not result:
				result=self.HasSubtree(pRoot1.right,pRoot2)
		return result

	# 判断树A中是否存在树B；若存在，则b先递归遍历完成，否则不存在；
	def DoesTree1haveTree2(self,pRoot1,pRoot2):
		if pRoot2==None:return True
		if pRoot1==None:return False
		if pRoot1.val!=pRoot2.val:
			return False
		return self.DoesTree1haveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right,pRoot2.right)



if __name__ == '__main__':
	bta=BinaryTree()
	btb=BinaryTree()

	bta.add(1)
	bta.add(2)
	bta.add(3)
	bta.add(4)
	bta.add(5)
	bta.add(6)
	bta.add(7)


	btb.add(1)
	btb.add(2)
	btb.add(3)
	btb.add(4)
	btb.add(7)

	s=Solution()
	print(s.HasSubtree(bta.root,btb.root))