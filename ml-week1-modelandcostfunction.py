# WEEK 1 - Model and Cost Function 

""" 
MODEL REPRESENTATION 

1. Training Set (of housing prices)
	-> (x, y) is a single row/training example 
2. Learning Algorithm 
3. Output Function (h for hypothesis) 
	-> h(x) = y_theta
	-> h is a function that maps from x to y 

	-> we represent h(x) literally as a y = mx + b but with whatever symbols ya want  
	-> starting with linear functions as a building block 
		-> specifically UNIVARIATE LINEAR REGRESSION for housing prices 




COST FUNCTION 
	-> how to fit the best possible straight line to our data 


	h_theta(x) = theta_0 + theta_1*x --> theta terms are parameters 

	With different parameters, we get different hypotheses. 

	BIG IDEA: Choose the theta_0 and theta_1 such that h_theta is close to your training examples. (least cost)
		-> How? Minimization function!


	FUNCTION: Minimize thetas 
		EXAMPLE: minimize squared value of (predicted house price - actual house price), summed from i to m (sum over training set, all x_i, y_i pairs), averaged.(multiplied by 1/2m term)
		
		"Find me the values of theta that minimize the average squared value of predicted minus actual over the training set."

		J(theta_0, theta_1) ==> Cost Function
		Squared Error function pretty common for regression


	EXTRA NOTE: why is the term 1/2? Makes it easier when taking the derivative during gradient descent b/c exp will cancel with 1/2. 




COST FUNCTION INTUITION
	
	We have hypothesis h(x), parameters theta_0 & theta_1, cost function J(theta_0, theta_1) , and goal minimize J(thetas).

	Given the cost plot (contour plot, in the case of two-dim function) for any point you select, the farther away you get from the minimum, the more expensive the cost of that line of fit becomes.
	

"""

