# desc:输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# solution:首先判断整数2进制表示中最右边一位是不是1，其次将整个数向右移动一位直至整个整数变成0；
# 判断最右边一位为1：将1与该数做位与运算&


def NumberOf1(n):
	count=0
	if(n<0):
		# m=~n+1
		# print(m)
		# python 没有位数的限制所以不能直接按位取反加1求补码

		n = n & 0xffffffff
		# print(bin(n))
	while(n):
		if(1&n==1):
			count=count+1
		n=n>>1
	return count


if __name__=="__main__":
	print(NumberOf1(-5))

