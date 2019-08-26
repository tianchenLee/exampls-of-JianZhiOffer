# SingleCycleLinkList.py
# 单向循环链表




class Node(object):
	def __init__(self,elem):
		self.elem=elem
		self.next=None




class SingleCycleLinkList(object):
	"""单向循环链表"""
	def __init__(self,node=None):
		self.__head=node 
		if node:
			node.next=node

	def empty(self):
		return	self.__head==None



	def length(self):
		if self.empty():
			return 0
		cur=self.__head
		count=1
		while cur.next is not  self.__head:
			count+=1
			cur=cur.next
		return count



	def travel(self):
		if self.empty():
			return 
		cur = self.__head
		while cur.next!=self.__head:
			print(cur.elem,end=" ")
			cur=cur.next
		# 退出循环的条件是cur指向尾节点
		# 尾节点的值还未打印
		# 同时打印
		# 只有一个节点的条件
		print(cur.elem)

	def add(self,elem):
		node=Node(elem)
		# node.next=self.__head
		# self.__head=node

		# while cur.next=!node.next:
		# 	cur=cur.next
		# cur.next=node
		
		if self.empty():
			self.__head=node
			node.next=node
		else:
			cur=self.__head
			while cur.next is not self.__head:
				cur=cur.next
			node.next=self.__head
			self.__head=node
			cur.next=node
			cur.next=self.__head

	def append(self,elem):
		node=Node(elem)
		if self.empty():
			self.__head=node
			node.node=node
		else:	
			cur=self.__head
			while (cur.next!=None):
				cur=cur.next
			node.next=self.__head
			cur.next=node

	def insert(self,pos,elem):
		if pos<=0:
			self.add(elem)
		elif(pos>self.length()-1):
			self.append()
		else:
			pre=self.__head
			count=0
			while count+1<pos:
				count+=1
				pre=pre.next
			node = Node(elem)
			node.next=pre.next
			pre.next=node


# 单向循环链表的remove比较复杂
# 1、判断是否为空，为空则返回
# 2、不为空则遍历，遍历的终止条件是 cur.next=self.head
	# 最后一个节点不被循环体处理：退出时判断最后一个元素是否需要被删除
	# 若是只有一个节点那循环不会进入，所以在循环外的情况需要判断；
# 3、若能进入循环体，
	# 没找到之前游标依次往后移动来遍历
	# 如果找到了需要判断
		#头节点：找尾节点更改其next域，rear来遍历，cur在头节点等待遍历完成；
		# 中间节点和单链表的节点相同
	def  remove(self,elem):
		if self.empty():
			return

		cur = self.__head
		pre=None
		while cur.next!=self.__head:
			if(cur.elem==elem):
				if cur==self.__head:
					# 头节点，头节点删除之后，尾节点的循环指向要改变
					# 所以需要找到尾节点
					# self.__head=cur.next
					rear=self.__head
					while rear.next is not self.__head:
						rear=rear.next
					self.__head=cur.next
					rear.next=self.__head
					rear
				else:
					# 中间节点，和单链表相同
					pre.next=cur.next
				return
			else:
				pre=cur
				cur=cur.next
		# 退出循环，cur指向尾节点，若为节点等于该元素，删除尾节点
		if(cur.elem is elem):
			if cur is self.__head:
				 self.__head=None
			pre.next=cur.next
		return False


	def search(self,elem):
		if self.empty():
			return False
		cur = self.__head
		while cur.next is not self.__head:
			if(cur.elem==elem):
				return True
			cur=cur.next
			if cur.elem is elem:
				return True
			return False
		return False




if __name__ == '__main__':
	scll=SingleCycleLinkList()

	scll.append(1)
	scll.append(2)
	scll.add(3)

	scll.travel()
	scll.insert(1,6)
	scll.travel()

	scll.remove(1)
	scll.remove(3)
	scll.remove(2)
	print(scll.search(3))
	print(scll.length())
	scll.travel()