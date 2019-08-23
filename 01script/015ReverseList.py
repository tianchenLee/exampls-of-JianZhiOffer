#desc 输入一个链表，反转链表后，输出新链表的表头。
#solution 


# 单链表的结点
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	"""单链表"""
class SingleLinkList(object):
	def __init__(self,node=None):
		self.__head = node


	def add(self, item):
		"""头部添加元素"""
		# 先创建一个保存item值的节点
		node = ListNode(item)
		# 将新节点的链接域next指向头节点，即_head指向的位置
		node.next = self.__head
		# 将链表的头_head指向新节点
		self.__head = node

	def travel(self):
		cur = self.__head

		while cur:
			print(cur.val,end=" ")
			cur=cur.next
		print("")


# 本地测试反转之后链表只留下反转前的第一个节点，其他全丢了
# 但是在牛客网提交通过
	# def ReverseList(self):
	#	 # write code here
	#	 cur = self.__head
	#	 pre = None
	#	 if(cur==None or cur.next==None):return cur
	#	 while cur:
	#	 	# 首先记录当前节点的下一个节点
	#	 	nnode = cur.next
	#	 	# 然后对当前节点进行反转
	#	 	cur.next=pre
	#	 	# 指针后移
	#	 	pre=cur
	#	 	cur=nnode
	#	 	# 如果当前节点还没有指向空，则进行下一轮循环
	#	 	# 最后一轮循环时：cur处于尾节点，cur.next指向空了；
	#	 	#nnode为空
	#	 	# cur指向反转
	#	 	# pre指向最后一个节点
	#	 	# cur后移，cur为空 退出循环
	#	 return pre


	def ReverseList(self):
		cur = self.__head
		pre = None
		if(cur==None or cur.next==None):return cur
		while cur:
			nnode = cur.next
			cur.next=pre
			pre=cur
			cur=nnode
		## pre才是反转之后的链表的头节点
		# cur已经指向空了
		# 使用pre.next可以遍历
		while pre:
			print(pre.val,end=" ")
			pre=pre.next
		print("")
		return pre


def main():
	ll=SingleLinkList()

	ll.add(1)
	ll.add(2)
	ll.add(3)
	ll.add(4)
	ll.add(5)
	ll.add(6)
	# add是头插，所以此时顺序是654321

	ll.travel()# 654321
	ll.ReverseList() # 列表反转
	ll.travel() # 123456

	ll.add(21)
	ll.add(23)

	ll.travel()# 654321
	ll.ReverseList() # 列表反转并遍历
	



if __name__ == '__main__':
	main()