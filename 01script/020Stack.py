# Stack by list

# Stack() 
# push() 压栈/入栈
# pop() 出栈
# peek()
# is_empty()
# size()


class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		super(Stack, self).__init__()
		# self.arg = arg
		self.__list=[]


	def push(self,arg):
		self.__list.append(arg)


	def pop(self):
		return self.__list.pop() # 顺序表的尾部操作时间复杂度是O1，链表的话则操作头部


	def peek(self):
		if(self.__list):
			self.__list[-1]
		else:
			return None

	def is_empty(self):
		return self.__list==[]
# == 返回逻辑值；如果为空返回真；
		# return not self.__list
	def size(self):
		return len(self.__list)

	def min(self):
		if(self.__list):
			return min(self.__list)
		else:
			return None

			
if __name__ == '__main__':
	
	stack=Stack()
	# stack.push("hello")
	# stack.push("world")
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)

	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())
	# print(stack.pop())


	print(stack.min())