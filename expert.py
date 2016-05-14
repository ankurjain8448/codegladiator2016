# ANKUR JAIN
max_row = 0
max_col = 0
main_ans = 10**10
main_ans_updated = False
min_tetris_count = None


def add_to_ans_array(val):
	t = long(val)
	global main_ans
	main_ans = min(main_ans,t)
	global main_ans_updated
	main_ans_updated = True
	global min_tetris_count
	if min_tetris_count == t:
		global max_row
		max_row = 0
		global max_col
		max_col = 0


def count_zero_in_matrix(matrix):
	return sum(1 for j in xrange(max_col) for i in xrange(max_row) if matrix[i][j] == 0)

def a(matrix,row,col,reverse=False):
	"""
		[1]
	   	[1]
	   	[1]
	"""
	if reverse :
		for i in xrange(3):
			matrix[row+i][col] = 0
		return matrix
	if max_row >= row+3 and [0,0,0] == [matrix[row+i][col] for i in xrange(3)]:
		for i in xrange(3):
			matrix[row+i][col] = 1
		return matrix , 1,3
	return matrix , 0 ,0


def b(matrix,row,col,reverse=False):
	"""
		[1,1,1]
	"""
	if reverse:
		matrix[row][col:col+3] = [0,0,0]
		return matrix
	if max_col>=col+3 and [0,0,0] == matrix[row][col:col+3] :
		matrix[row][col:col+3] = [1,1,1]
		return matrix , 1 ,3
	return matrix , 0 ,0


def c(matrix,row,col,reverse=False):
	"""
		[1,1,1]
	   	[ ,1, ]
	"""
	if reverse:
		matrix[row][col:col+3] = [0,0,0]
		matrix[row+1][col+1] = 0
		return matrix
	if max_col>=col+3 and max_row>=row+2 and [0,0,0] == matrix[row][col:col+3] and matrix[row+1][col+1]==0:
		matrix[row][col:col+3] = [1,1,1]
		matrix[row+1][col+1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def d(matrix,row,col,reverse=False):
	"""
		[ ,1, ]
		[1,1,1]
	"""
	if reverse:
		for i in xrange(col-1,col+2):
			matrix[row+1][i] = 0
		matrix[row][col] = 0
		return matrix
	if max_col>=col+2 and max_row>=row+2 and col-1>-1  and [0,0,0] == matrix[row+1][col-1:col+2] and matrix[row][col]==0:
		for i in xrange(col-1,col+2):
			matrix[row+1][i] = 1
		matrix[row][col] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def e(matrix,row,col,reverse=False):
	"""
		[1]
	   	[1,1]
	   	[1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col] = 0
		matrix[row+1][col+1]=0
		return matrix
	if max_row >= row+3 and max_col>=col+2 and [0,0,0] == [matrix[i][col] for i in xrange(row,row+3)] and matrix[row+1][col+1]==0:
		for i in xrange(row,row+3):
			matrix[i][col] = 1
		matrix[row+1][col+1]=1
		return matrix , 1,4
	return matrix , 0 ,0


def f(matrix,row,col,reverse=False):
	"""
		[1]
	  [1,1]
	   	[1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col] = 0
		matrix[row+1][col-1]=0
		return matrix
	if max_row >= row+3 and -1>col-1 and [0,0,0] == [matrix[i][col] for i in xrange(row,row+3)] and matrix[row+1][col-1]==0:
		for i in xrange(row,row+3):
			matrix[i][col] = 1
		matrix[row+1][col-1]=1
		return matrix , 1,4
	return matrix , 0 ,0


def g(matrix,row,col,reverse=False):
	"""
		[1,1,1]
	   	[ , ,1]
	"""
	if reverse:
		for i in xrange(col,col+3):
			matrix[row][i] = 0
		matrix[row+1][col+2] = 0
		return matrix
	if max_col>=col+3 and max_row>=row+2 and [0,0,0] == matrix[row][col:col+3] and matrix[row+1][col+2]==0:
		for i in xrange(col,col+3):
			matrix[row][i] = 1
		matrix[row+1][col+2] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def h(matrix,row,col,reverse=False):
	
	"""
		[ , ,1]
		[1,1,1]
	"""
	if reverse:
		matrix[row+1][col]=0
		matrix[row+1][col-1] = 0
		matrix[row+1][col-2] = 0
		matrix[row][col] = 0
		return matrix
	if max_col>=col+1 and -1>col-3 and max_row>=row+2 and 0== matrix[row+1][col] and 0== matrix[row+1][col-1] and 0== matrix[row+1][col-2] and matrix[row][col]==0:
		matrix[row+1][col]=1
		matrix[row+1][col-1] = 1
		matrix[row+1][col-2] = 1
		matrix[row][col] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def i(matrix,row,col,reverse=False):
	"""
		[1,1]
		[1,1]
	"""
	if reverse:
		matrix[row][col] = 0;matrix[row][col+1] = 0;matrix[row+1][col] = 0;matrix[row+1][col+1] = 0
		return matrix
	if max_col>=col+2 and max_row>=row+2 and [0,0] == matrix[row][col:col+2] and [0,0] == matrix[row+1][col:col+2]:
		matrix[row][col] = 1;matrix[row][col+1] = 1;matrix[row+1][col] = 1;matrix[row+1][col+1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def j(matrix,row,col,reverse=False):
	"""
		  [1,1]
		[1,1]
	"""
	if reverse:
		matrix[row][col] = 0;matrix[row][col+1] = 0;matrix[row+1][col] = 0;matrix[row+1][col-1] = 0
		return matrix
	if max_col>=col+2 and max_row>=row+2 and -1 > col-1 and [0,0] == matrix[row][col:col+2] and matrix[row+1][col]==0 and matrix[row+1][col-1]==0:
		matrix[row][col] = 1;matrix[row][col+1] = 1;matrix[row+1][col] = 1;matrix[row+1][col-1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def k(matrix,row,col,reverse=False):
	"""
		[1,1]
		  [1,1]
	"""
	if reverse:
		matrix[row][col] = 0;matrix[row][col+1] = 0;matrix[row+1][col+2] = 0;matrix[row+1][col+1] = 0
		return matrix
	if max_col>=col+3 and max_row>=row+2 and [0,0] == matrix[row][col:col+2] and [0,0] == matrix[row+1][col+1:col+3] :
		matrix[row][col] = 1;matrix[row][col+1] = 1;matrix[row+1][col+2] = 1;matrix[row+1][col+1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def l(matrix,row,col,reverse=False):
	"""
		[1,1]
		[1]
		[1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col] = 0
		matrix[row][col+1] = 0
		return matrix
	if max_row >= row+3 and max_col >= col+2 and [0,0,0] == [matrix[i][col] for i in xrange(row,row+3)] and matrix[row][col+1]==0:
		for i in xrange(row,row+3):
			matrix[i][col] = 1
		matrix[row][col+1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def m(matrix,row,col,reverse=False):
	"""
	  [1,1]
		[1]
		[1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col+1] = 0
		matrix[row][col] = 0
		return matrix
	if max_row >= row+3 and max_col >= col+2 and [0,0,0] == [matrix[i][col+1] for i in xrange(row,row+3)] and matrix[row][col]==0:
		for i in xrange(row,row+3):
			matrix[i][col+1] = 1
		matrix[row][col] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def n(matrix,row,col,reverse=False):
	"""
		[1]
		[1]
	  [1,1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col] = 0
		matrix[row+2][col-1] = 0
		return matrix
	if max_row >= row+3 and -1>col-1 and [0,0,0] == [matrix[i][col] for i in xrange(row,row+3)] and matrix[row+2][col-1]==0:
		for i in xrange(row,row+3):
			matrix[i][col] = 1
		matrix[row+2][col-1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def o(matrix,row,col,reverse=False):
	"""
		[1]
		[1]
	    [1,1]
	"""
	if reverse:
		for i in xrange(row,row+3):
			matrix[i][col] = 0
		matrix[row+2][col+1] = 0
		return matrix
	if max_row >= row+3 and max_col>=col+2 and [0,0,0] == [matrix[i][col] for i in xrange(row,row+3)] and matrix[row+2][col+1]==0:
		for i in xrange(row,row+3):
			matrix[i][col] = 1
		matrix[row+2][col+1] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def p(matrix,row,col,reverse=False):
	"""
		[1]
		[1,1,1]
	"""
	if reverse:
		matrix[row+1][col:col+3] = [0,0,0]
		matrix[row][col] = 0
		return matrix
	if max_col>=col+3 and max_row>=row+2 and [0,0,0] == matrix[row+1][col:col+3] and matrix[row][col] == 0:
		matrix[row+1][col:col+3] = [1,1,1]
		matrix[row][col] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def q(matrix,row,col,reverse=False):
	"""
		[1,1,1]
		[1]
	"""
	if reverse:
		matrix[row][col:col+3] = [0,0,0]
		matrix[row+1][col] = 0
		return matrix
	if max_col>=col+3 and max_row>=row+2 and [0,0,0] == matrix[row][col:col+3] and matrix[row+1][col]==0:
		matrix[row][col:col+3] = [1,1,1]
		matrix[row+1][col] = 1
		return matrix , 1,4
	return matrix , 0 ,0


def r(matrix,row,col,reverse=False):
	"""
		[1]
		[1,1]
		  [1]
	"""
	if reverse:
		matrix[row][col]=0;matrix[row+1][col]=0;matrix[row+1][col+1]=0;matrix[row+2][col+1]=0
		return matrix
	if max_row >= row+3 and max_col >= col+2 and matrix[row][col]==0 and matrix[row+1][col]==0 and matrix[row+1][col+1]==0 and matrix[row+2][col+1]==0:
		matrix[row][col]=1;matrix[row+1][col]=1;matrix[row+1][col+1]=1;matrix[row+2][col+1]=1
		return matrix , 1,4
	return matrix , 0 ,0


def s(matrix,row,col,reverse=False):
	"""
		  [1]
		[1,1]
		[1]
	"""
	if reverse:
		matrix[row][col]=0;matrix[row+1][col]=0;matrix[row+1][col-1]=0;matrix[row+2][col-1]=0 
		return matrix
	if max_row >= row+3 and -1 >= col-1 and matrix[row][col]==0 and matrix[row+1][col]==0 and matrix[row+1][col-1]==0 and matrix[row+2][col-1]==0:
		matrix[row][col]=1;matrix[row+1][col]=1;matrix[row+1][col-1]=1;matrix[row+2][col-1]=1 
		return matrix , 1,4
	return matrix , 0 ,0


def fill_matrix(actual_matrix,row,col,currentTetrisCount):
	
	updated_matrix,tetris_count,filled_ones =  a(actual_matrix,row,col)
	if tetris_count > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  a(actual_matrix,row,col,True)
	
	updated_matrix,tc,filled_ones =  b(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  b(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  c(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  c(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  d(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  d(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  e(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  e(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  f(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  f(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  g(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  g(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  h(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  h(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  i(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  i(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  j(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  j(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  k(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  k(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  l(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  l(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  m(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  m(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  n(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  n(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  o(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  o(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  p(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  p(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  q(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  q(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  r(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  r(actual_matrix,row,col,True)

	updated_matrix,tc,filled_ones =  s(actual_matrix,row,col)
	if tc > 0:
		temp_tetris_count = super_function(updated_matrix,currentTetrisCount+1)
		updated_matrix =  s(actual_matrix,row,col,True)
	
	return updated_matrix,0,filled_ones


def super_function(matrix, currentTetrisCount):
	"""
		moves in matrix and fills matrix  
	"""
	global main_ans		
	if currentTetrisCount == main_ans:
		return currentTetrisCount
	ans = 0
	temp_i =0 ; temp_j = 0;
	flag = False
	for i in xrange(max_row):
		for j in xrange(max_col):
			if matrix[i][j]==0:
				temp_i = i;temp_j = j
				flag = True
				break
		if flag:
			break
	if flag:
		matrix,tetris_count,filled_one = fill_matrix(matrix,temp_i,temp_j, currentTetrisCount)
	else :
		"""matrix_filled"""
		add_to_ans_array(currentTetrisCount)

	return currentTetrisCount

def reset_globals():
	global max_row
	max_row = 0
	global max_col
	max_col = 0
	global main_ans
	main_ans = 10**10
	global main_ans_updated
	main_ans_updated = False
	global min_tetris_count
	min_tetris_count = None



def requiredTetriminos(input1,input2,input3):
	global max_row
	max_row = input1
	global max_col
	max_col = input2
	matrix = [[input3[max_col*i +j] for j in xrange(max_col)] for i in xrange(max_row)]
	empty_blocks  = count_zero_in_matrix(matrix)
	
	temp_val = 0
	if empty_blocks%4 != 0 :
		temp_val = int(empty_blocks/4)+ 1
	else :
		temp_val = int(empty_blocks/4)
	global min_tetris_count
	min_tetris_count = temp_val
	
	ans = super_function(matrix,0)
	
	matrix = None
		
	min_tetris_count = None
	global main_ans_updated
	if main_ans_updated :
		global main_ans
		temp = main_ans
		reset_globals()
		return temp
	reset_globals()
	return 0

# 47.28 Seconds with deepcopy --> managed to 4.42 seconds  --> 0.1 second
print requiredTetriminos(3,2,[1,1,1,1,1,1])
print requiredTetriminos(3,2,[0,0,0,0,0,0])
print requiredTetriminos(3,3,[1,1,1,0,0,0,0,0,0])
print requiredTetriminos(3,3,[0,0,0,0,0,0,0,0,0])
print requiredTetriminos(3,3,[1,1,1,0,1,0,0,0,0])
print requiredTetriminos(3,5,[1,1,0,1,1,1,0,0,0,1,1,0,0,0,1])
print requiredTetriminos(4,8,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1])