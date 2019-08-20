# 007 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。 n<=39
# 第3个位置起任意一个位置的数据为前两个位置的数据和
def func(n):
	a=0
	b=1
	for i in range(n):
		a,b=b,a+b
	print(a)

def main():
	n=int(input("请输入："))
	func(n)


if __name__ == '__main__':
	main()
