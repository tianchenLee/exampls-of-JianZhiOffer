
# 输入一个链表，输出该链表中倒数第k个结点。
# 链表的遍历


# 单链表的结点
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	"""单链表"""
class SingleLinkList(object):
	def __init__(self):
		self._head = None


	def add(self, item):
		"""头部添加元素"""
		# 先创建一个保存item值的节点
		node = ListNode(item)
		# 将新节点的链接域next指向头节点，即_head指向的位置
		node.next = self._head
		# 将链表的头_head指向新节点
		self._head = node


	# 代码思路：两个指针，都先指向头结点，然后让第一个指针走k-1步；到达第k个节点，
	# 然后两个指针同时往后移，当第一个节点到达末尾的时候，第二个节点所在位置就是倒数第k个节点了
	# 参考：https://www.nowcoder.com/profile/7411547/codeBookDetail?submissionId=12655252
	def FindKthToTail(self,k):
		front=self._head
		later=self._head
		for i in range(k):
			if front==None:
				return
			if front.next == None and i==k-1:
				return self._head
			front = front.next
		while front.next !=None:
			front = front.next
			later = later.next
		return later.next



def main():
	ll=SingleLinkList()

	ll.add(1)
	ll.add(2)
	ll.add(3)
	ll.add(4)
	ll.add(5)
	ll.add(6)
	ll.FindKthToTail(3)


if __name__ == '__main__':
	main()