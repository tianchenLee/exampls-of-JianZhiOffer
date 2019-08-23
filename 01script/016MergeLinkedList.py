# MergeLinkedList.py
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

# 合并排序

# 单链表的结点
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	"""单链表"""
class SingleLinkList(object):
	def __init__(self,node=None):
		self.head = node


	def add(self, item):
		"""头部添加元素"""
		# 先创建一个保存item值的节点
		node = ListNode(item)
		# 将新节点的链接域next指向头节点，即_head指向的位置
		node.next = self.head
		# 将链表的头_head指向新节点
		self.head = node


	def append(self,item):
		node=ListNode(item)
		if self.head==None:
			self.head=node
		else:
			cur=self.head
			while cur.next:
				cur=cur.next
			cur.next=node
	

	def travel(self):
		cur = self.head

		while cur:
			print(cur.val,end=" ")
			cur=cur.next
		print("")




# 合并两个单链表
def MergeLinkedList(ll1,ll2):
	pHead1=ll1.head
	pHead2=ll2.head
	# 若存在一个链表为空则直接返回另一个
	if pHead1 is None:
		return pHead2
	elif pHead2 is None:
		return pHead1

	# 比较大小选取头节点
	elif pHead1.val>pHead2.val:
		cur=pHead2
		pHead2=pHead2.next
	else:
		cur=pHead1
		pHead1=pHead1.next

	# 先记录当前的头节点，之后使用游标cur去遍历比大小
	head=cur
	while pHead1 is not None and pHead2 is not None:
		# 这里是不稳定的，因为如果遇到了两个链表中的值相同的情况，那么他们前后的排列是根据指针当前的指向决定的，但是指针的指向是根据前两个节点的比较决定的，在每次输入不同的前置节点的情况下，这里相同大小数据的位置可能会发生前后变化
		if pHead1.val>pHead2.val:
			cur.next=pHead2
			pHead2=pHead2.next
		else:
			cur.next=pHead1
			pHead1=pHead1.next
		cur=cur.next
	if pHead1 is not None:
		cur.next=pHead1
	if pHead2 is not None:
		cur.next=pHead2
	return head


if __name__ == '__main__':
	l=SingleLinkList()
	ll=SingleLinkList()

	l.append(2)
	l.append(7)
	l.append(9)
	l.append(18)

	ll.append(1)
	ll.append(7)
	ll.append(9)
	ll.append(14)


	lll=MergeLinkedList(l,ll)

		
	while lll:
		print(lll.val,end=" ")
		lll=lll.next
	print("")