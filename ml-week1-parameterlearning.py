# WEEK 1 - Parameter Learning 

"""

GRADIENT DESCENT ALGORITHM  

	-> A general algorithm to minimize the cost function J. In this case, for LR.

		-> BIG IDEA
			1. Start with some initial guesses for theta_0...theta_n
			2. Keep changing theta_0....theta_n until J(thetas) hits eventually, hopefully, hits some minimum 

		1. If standing at some point in this hilly landscape, at each step, we look around us and ask "If we take a baby step in some direction, what direction should I go if I want to walk down as rapidly as possible?"

		2. Now you're at a new point, and repeat step 1. 

		--> Eventually, you will land at some local minimum! 


		-> MATH
			Repeat until convergence: 
				theta_j := theta_j - alpha * part.deriv wrt theta_j of J(theta_0, theta_1)

				alpha -> learning rate (large alpha is aggressive learning rate. small alpha is baby steps)

				We do this for j=0, j=1, as in, simultaneous updates for theta_0, theta_1. 

			****SIMULTANEOUS UPDATE IMPLEMENTATION:**** IN THIS ORDER!!!

			temp0 := theta_0 - alpha * derivative wrt theta_0 of J(theta_0, theta_1)
			temp1 := theta_1 - alpha * derivative wrt theta_1 of J(theta_0, theta_1)

			theta_0 = temp0
			theta_1 = temp1


GRADIENT DESCENT INTUITION 

	-> General Algorithm: update theta as follows ==> 
		theta = theta - learning_rate * partial_derivative(cost_func(theta))

		In this example, the second term (learning_rate * part_deriv(cost_func(theta))) evaluates positively, so we move theta to the left
		 -> In a convex function where we start to the right of the minimum, that means we're moving toward the minimum! 


		Now, let's initialize theta to the left of minimum. 
		 -> The derivative at initialized theta will be negative. The second term will evaluate to something negative, so we're minusing a negative, and increasing overall theta, moving to right. 
		 -> We are still moving toward the minimum! 


	-> REMINDER: Slope is the third side of a triangle w a right angle that lines up tangent to a point in the function hehe 


	ALPHA -> adjust alpha such that GD converges in reasonable time. 

		=> What if too small? 
			Gradient descent will be slow. 

		=> What if too big? 
			It can overshoot the minimum. Fail to converge or even diverge. (theta zig zags across the convex function, slowly moving up y axis) 



GRADIENT DESCENT FOR LINEAR REG 
		
		=== SIMULTANEOUS UPDATES FOR THETA_0 AND THETA_1 ===

		repeat until convergence -> 

		theta_0 = theta_0 - (alpha) * (1/m)(sum from 1 to m (h_0(xi) - yi))
		theta_1 = theta_1 - (alpha) * (1/m)(sum from 1 to m (h_0(xi) - yi)) * (xi)

		In both cases, the second term (after alpha) is the partial derivative WRT theta_0 or theta_1 (depending on the term), with theta_0 = 0 and theta_1 = 1.
	
				=> sooooo cost function for linear reg is always going to be convex (in 3d) and will have on global optimum. always converges :) 

		Batch Gradient Descent: at each step of alg, uses all the training samples. (this is the "sum" term, from 1 to m)


		NOTE: to solve for minimum numerically, study advanced linalg and use normal equations method. 
			  -> GD interatively scales a bit better 















