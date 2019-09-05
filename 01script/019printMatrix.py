# printMatrix.py
# 参考自：https://blog.csdn.net/yangnianjinxin/article/details/79243110
# def printMatrix(matrix):
# 	# write code here
# 	if matrix==[[]]:
# 		return
# 	row=len(matrix)
# 	column=len(matrix[0])
# 	start=0
# 	res=[]
# 	while row>start*2 and column>start*2:
# 		endX=column-1-start
# 		endY=row-1-start
# 		#从左到右打印一行
# 		for i in range(start,endX+1):
# 			res.append(matrix[start][i])
# 			#print(matrix[start][i])
# 		#从上往下打印一列
# 		if start<endY:
# 			for i in range(start+1,endY+1):
# 				res.append(matrix[i][endX])
# 				#print(matrix[i][endX])
# 		#从右到左打印一行
# 		if start<endX and start<endY:
# 			for i in range(endX-1,start-1,-1):
# 				res.append(matrix[endY][i])
# 				#print(matrix[endY][i])
# 		#从下到上打印一列
# 		if start<endX and start<endY-1:
# 			for i in range(endY-1,start,-1):
# 				res.append(matrix[i][start])
# 				#print(matrix[i][start])
# 		start+=1
# 	return res

# # 1 2 3
# # 1 3 2
# # 1 4 5

# matrix=[[1,2,3],[1,3,2],[1,4,5]]

# print(printMatrix(matrix))






class Solution:
	# matrix类型为二维列表，需要返回列表
	def printMatrix(self, matrix):
		# write code here
		result = []
		while(matrix):
			result+=matrix.pop(0)
			if not matrix or not matrix[0]:
				break
			matrix = self.spiralOrder(matrix)
		return result

	# 牛客课后解答，旋转递归，思维巧妙
	def spiralOrder(self, matrix):
			#return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
		num_r = len(matrix)
		num_c = len(matrix[0])
		newmat = []
		for i in range(num_c):
			newmat2 = []
			for j in range(num_r):
				newmat2.append(matrix[j][i])
			newmat.append(newmat2)
		newmat.reverse()
		return newmat


if __name__ == '__main__':
	s=Solution()
	matrix=[[1,2,3],[1,3,2],[1,4,5]]
	print(s.printMatrix(matrix))