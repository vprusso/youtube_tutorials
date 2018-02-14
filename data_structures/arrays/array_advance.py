def array_advance(A):

	furthest_reached = 0
	last_idx = len(A) - 1
	i = 0
	while i <= furthest_reached and furthest_reached < last_idx:		
		furthest_reached = max(furthest_reached, A[i] + i)
		#print("i: " + str(i))
		#print("A[i]+i: " + str(A[i] + i))
		#print("furthest_reached: " + str(furthest_reached))			
		
		i += 1
	
	#print("i: " + str(i))
	#print("A[i]+i: " + str(A[i] + i))
	#print("furthest_reached: " + str(furthest_reached))	
	return furthest_reached >= last_idx

# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3,3,1,0,2,0,1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3,2,0,0,2,0,1]
print(array_advance(A))
