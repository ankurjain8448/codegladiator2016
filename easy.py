max_row = 0
max_col = 0
def reset_globals():
	global max_row
	max_row = 0
	global max_col
	max_col = 0

def count_neighbour(matrix, i, j):
	# neighbour means filled with 1's
	count = 0
	
	if -1 < i -1 :
		
		if matrix[i-1][j] in [1,-1]:
			count+=1
		if -1 < j-1 and matrix[i-1][j-1] in [1,-1]:
			count+=1
		if j+1 < max_col  and matrix[i-1][j+1] in [1,-1]:
			count+=1
	
	if -1 < j-1 and matrix[i][j-1] in [1,-1]:
		count+=1
	
	if j+1 < max_col and matrix[i][j+1] in [1,-1]:
		count+=1
	
	if i+1 < max_row :
		
		if -1 < j-1 and matrix[i+1][j-1] in [1,-1]:
			count+=1
		if matrix[i+1][j] in [1,-1]:
			count+=1
		if j+1 < max_col and matrix[i+1][j+1] in [1,-1]:
			count+=1
	
	return count


# def print_matrix(matrix):
# 	for i in matrix:
# 		print i
# 	print "hi"

def make_generation(matrix,s1,s2,b1,b2):
	has_any_element_changes_in_pass = False
	for i in xrange(max_row):
		for j in xrange(max_col):
			# print "current index (%d,%d)" % (i,j)
			count = count_neighbour(matrix,i,j)
			# print "after current index (%d,%d)" % (i,j)
			if matrix[i][j] == 1:
				if count < s1 or count > s2 :
					matrix[i][j] = -1; has_any_element_changes_in_pass = True
			else:
				if count >= b1 and count <= b2 :
					matrix[i][j] = 'b';has_any_element_changes_in_pass = True

	return matrix , has_any_element_changes_in_pass

def fill_generation(matrix):
	for i in xrange(max_row):
		for j in xrange(max_col):
			if matrix[i][j] == -1 :
				matrix[i][j] = 0
			elif matrix[i][j] == 'b':
				matrix[i][j] = 1
	return matrix


def survivalcells(input1,input2):
	
	row,col, s1,s2,b1,b2,g = input1
	global max_row
	max_row = row
	global max_col
	max_col = col

	matrix = []
	index = 0
	for i in xrange(max_row):
		temp = []
		for j in xrange(max_col):
			temp.append(input2[index])
			index+=1
		matrix.append(temp)
	
	# g times iteration over the matrix
	# print print_matrix(matrix)
	# print "above is the initial matrix"
	for _ in xrange(g):
		matrix, has_any_element_changes_in_pass = make_generation(matrix,s1,s2,b1,b2)
		if not has_any_element_changes_in_pass:
			break
		matrix = fill_generation(matrix)
		# print print_matrix(matrix)
		# print "-----------------------"
	temp = []
	for i in matrix:
		temp = temp + i
	reset_globals()
	return temp

import time
t1 = time.time()
print survivalcells([6,6,2,3,3,3,2],[0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1])
print survivalcells([3,4,2,3,3,3,3],[0,1,0,0,0,1,1,0,1,0,1,0])
print survivalcells([3,4,2,3,3,3,4],[0,0,1,1,0,1,0,1,0,0,0,0])
print time.time() - t1