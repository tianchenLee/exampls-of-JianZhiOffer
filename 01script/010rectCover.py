# desc:我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# solution：如果第一个竖着放则剩下n-1种情况；如果第一块横着放则第二块也要横着放在下面，剩下n-2种情况；故f(n)=f(n-1)+f(n-2),斐波那契的变形
def rectCover(n):
	if n<0:return 0
	else:
		a=1
		b=1
		for i in range(n):
			a,b=b,a+b
		return a 


if __name__ == '__main__':
	print(rectCover(int(input("请输入n的值："))))