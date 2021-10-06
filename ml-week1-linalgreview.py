# WEEK 1 - Linalg review 


"""
MATRICES AND VECTORS 

	=> Notation for matrix size
	=> Notation for referring to specific elements in matrices 


ADDITION + SUBTRACTION 
	
	=> You can only add matrices of the same dims. Result will be same dims. 
	=> Scalar multiplication, multiply all elements by the scalar. 


MATRIX VECTOR MULTIPLICATION 

	=> Inner dims have to match. 
	=> Result is outer dims! 

	=> Multiply columns by rows. 

	
	PREDICTION = DATA MATRIX * PARAMETERS -> writing code this way is simpler and more computationally efficient

""" 

# Initialize matrix A 
A = [1, 2, 3; 4, 5, 6;7, 8, 9] 

# Initialize vector v 
v = [1; 1; 1] 

# Multiply A * v
Av = A * v
 
 """ 

 MATRIX MULTIPLICATION * SPECIAL PROPERTIES 