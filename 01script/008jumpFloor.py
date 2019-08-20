# 008 青蛙跳台阶：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# 本地测试通过 但是在nowcoder系统中超过时间限制
def jumpFloor(number):
    # write code here
    if(number<=0):
    	return -1
    elif (number<=2):
    	return number
    else:
    	n_jump = jumpFloor(number-1)+jumpFloor(number-2)
    	return n_jump


def main():
	n=int(input("请输入台阶数："))
	print(jumpFloor(n))


if __name__ == '__main__':
	main()
