# 链表
# LinkedList.py


# 节点
class Node(object):
	def __init__(self,elem):
		self.elem=elem
		self.next=None
	""" self 代表类的实例，所以类内部的self对象中增加self.next属性相当于给类增加了next方法，以后该类实例化的所有对象中均存在该方法；"""
	# 上边这种注释可以通过方法调用查看,__doc__
# class Node(object):
#	 """节点"""
#	 def __init__(self, elem):
#		 self.elem = elem
#		 self.next = None



class SingleLinkList(object):

	def __init__(self,node=None):
		# head是单链表结构中维护的，只供内部函数使用，所以设置为私有属性
		# 单链表是由head和归纳法单方向推出来的，因此要定义head
		# 初始化时可以设置为空链表
		# 也可以先构建一个node，让node为单链表的头节点
		self.__head=node 
	# def __init__(self, node=None):
	#	 self.__head = node


	def empty(self):
		# 如果不为空则head指向某一值,head不指向某一值则为空
		return	self.__head==None
	# def is_empty(self):
	#	 """链表是否为空"""
	#	 return self.__head == None


	# def length(self):
	# 	"""链表长度"""
	# 	# 求长度需要一次从头到尾的遍历过程
	# 	# 找一个指针从头数到尾，cursor首先指向head所指向的地址
	# 	cur=self.__head
	# 	# 记录数量的count变量
	# 	count=0
	# 	# count=0记录的话空链表时候的特殊情况也能处理
	# 	# 但是如果count初始值为1的话需要处理空链表的情况
	# 	# 此外，count初始值为1的话cur.next为None就OK了，
	# 	while cur!=None:
	# 		# print("**********") # 会一直输出*** ，死循环，为空的时候，没有死循环
	# !!!!!!!!!!!# 是因为append方法中少写了一下else导致数据一直在不停的插入，所以这里的length一直在增加
	# 		count+=1
	# 		cur=cur.next
	# 	return count




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
			print(cur.elem,end=" ")
			cur=cur.next

	# 头插，先将新节点的next指向head指向的节点，再将head指向新节点，最后head断开
	def add(self,item):
		node=Node(item)
		node.next=self.__head
		self.__head=node


	# 尾插
	def append(self,item):
		node=Node(item)
		if self.empty():
			self.__head=node
		else:	
			cur=self.__head
			while (cur.next!=None):
				cur=cur.next
				print(count)
			cur.next=node

	def insert(self,pos,item):
		"""
		:param pos从0开始
		"""
		if pos<0:
			self.add(item)
		elif(pos>self.length()-1):
			self.append()
		else:
			pre=self.__head
			count=0
			while count<pos:
				count+=1
				pre=pre.next
			node = Node(item)
			node.next=pre.next
			pre.next=node

	def  remove(self,item):
		# 遍历的时候移除一个

	def search(self,item):
		## 遍历的时候加一个比对的步骤



if __name__ == '__main__':
	ll=SingleLinkList()

	print(ll.empty())
	print(ll.length())



	ll.append(12)

	ll.add(10)

	print(ll.empty())
	print(ll.length())
	ll.travel()

	ll.insert(1,112)
	ll.travel()