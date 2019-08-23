# DoubleLinkList.py

from LinkedList import SingleLinkList

class Node(object):
	"""Node,拥有前驱节点和后继节点位置存储区的结点"""
	def __init__(self, item):
		self.item = item
		self.next=None
		self.prev=None


class DoubleLinkList(SingleLinkList):
	"""DoubleLinkList,双向链表"""
	# 链表构造，判断为空，长度和遍历和单链表完全相同；
	# 按照面向对象可以直接继承 SingleLinkList 类
	def __init__(self, node=None):
		self.__head =node


	def empty(self):
		return	self.__head == None



	def length(self):
		cur=self.__head
		count=0
		while cur!=None:
			count+=1
			cur=cur.next
		return count


	def travel(self):
		cur = self.__head
		while cur!=None:
			print(cur.item,end=" ")
			cur=cur.next
		print("")




	# 前驱后继均需要改变
	def add(self,item):
		node=Node(item)
		if self.empty():
			self.__head=node
		else:
			node.next=self.__head
			self.__head=node
			# 因为是双向链表，所以next和pre都需要考虑
			node.next.prev=node


	def append(self,item):
		node=Node(item)
		if self.empty():
			self.__head=node
		else:	
			cur=self.__head
			while (cur.next!=None):
				cur=cur.next
				# print(count)
			cur.next=node
			node.prev=cur

	def insert(self,pos,item):
		if pos<=0:
			self.add(item)
		elif(pos>self.length()-1):
			self.append(item)
		else:
			cur=self.__head
			count=0
			while count<pos:
				count+=1
				cur=cur.next
			node = Node(item)
			node.next=cur
			node.prev=cur.prev
			cur.prev.next=node
			cur.prev=node
			

	def  remove(self,item):
		cur = self.__head
		pre=None
		while cur!=None:
			if(cur.item==item):
				if cur==self.__head:
					self.__head=cur.next
					if cur.next:
						cur.next.prev=None
				else:
					pre.next=cur.next
					if cur.next:
						pre.next.prev=pre
				break
			else:
				pre=cur
				cur=cur.next
		return False


	def search(self,item):
		cur = self.__head
		while cur!=None:
			if(cur.item==item):
				return True
			cur=cur.next
		return False


if __name__ == '__main__':
	dll=DoubleLinkList()
	dll.add(3)
	dll.add(5)

	dll.append(20)

	dll.insert(1,1)
	dll.insert(-2,0)
	dll.insert(8,7)

	dll.travel()
	dll.remove(0)
	dll.travel()

	print(dll.search(1))