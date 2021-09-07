import math
import numpy as np
import matplotlib.pyplot as plt

def scaled_partial_pivoting(a,b,c,d,e,f):
	r = 0
	val = 0
	i3 = 0
	u = 0
	k = 0
	extra_matrix = []
	good_matrix = a
	while i3 in range(len(a)):
		i3 += 1
		for i in range(len(a)):
			for i1 in range(len(a[i])):
				if (abs(a[i][i1]) > b[i]):
					b[i] = abs(a[i][i1])
				else:
					continue
		for i in range(len(b)):
			if ((c[i]/b[i]) > d):
				d = (c[i]/b[i])
				if len(good_matrix) == 4:
					e = 3
				elif (len(good_matrix) == 3):
					e = 2
				elif (len(good_matrix) == 2):
					e = 1
				elif (len(good_matrix) == 1):
					e = 0
				elif (i == len(b)-1 and (c[i]/b[i] <= d)):
					q = c[e]
					t = c[0]
					c[0] = c[e]
					c[e] = t
					r = e
					e = 0
					pass
				else:
					pass
			else:
				pass
		k = r
		for i in range(len(good_matrix)):
			for i1 in range(len(good_matrix[r])):
				val = good_matrix[i][u]/good_matrix[r][u]
				extra_matrix.append(good_matrix[r][i1])
				extra_matrix[i1] = (good_matrix[r][i1])*val
				if (good_matrix[i] != good_matrix[r]):
					good_matrix[i][i1] = good_matrix[i][i1] - extra_matrix[i1]
				else:
					print(a)
					pass
		del good_matrix[r]
		val = 0
		r = 0
		u += 1
		extra_matrix = []
	return good_matrix,b,c,d,e,f

matrix = [[1,-1,2,1],[3,2,1,4],[5,-8,6,3],[4,2,5,3]]
scale_vector = [0,0,0,0]
index_vector = [1,2,3,4]
soln_vector = [1,1,1,-1]
ratio_val = 0
i_cout = 1
l_cout = 0
print(scaled_partial_pivoting(matrix,scale_vector,index_vector,ratio_val,i_cout,l_cout))