


# 009 变态台阶跳：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 思路：小青蛙要跳到第n级台阶，对于n以前的任意一级台阶都可以选择落下or不落下
def jumpFloorII(number):
    # write code here
    if number<=0:
        return 0
    else:
        return 2**(number-1)


def main():
	n=int(input("请输入台阶数："))
	print(jumpFloorII(n))


if __name__ == '__main__':
	main()
