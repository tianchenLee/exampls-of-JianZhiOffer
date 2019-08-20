# desc:给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# solution:python的底层优化可直接调用函数pow

def Power(base, exponent):
    return pow(base,exponent)


if __name__ == '__main__':
	print(Power(2,3.5))