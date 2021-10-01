# WEEK 1 - Parameter Learning 

"""

GRADIENT DESCENT (Univariate Linear Reg) 

	-> A general algorithm to minimize the cost function J. In this case, for LR.

		-> BIG IDEA
			1. Start with some initial guesses for theta_0...theta_n
			2. Keep changing theta_0....theta_n until J(thetas) hits eventually, hopefully, hits some minimum 

		1. If standing at some point in this hilly landscape, at each step, we look around us and ask "If we take a baby step in some direction, what direction should I go if I want to walk down as rapidly as possible?"

		2. Now you're at a new point, and repeat step 1. 

		--> Eventually, you will land at some local minimum! 


		-> MATH
			Repeat until convergence: 
				theta_j := theta_j - alpha * derivative wrt theta_j of J(theta_0, theta_1)

				alpha -> learning rate (large alpha is aggressive learning rate. small alpha is baby steps)

				We do this for j=0, j=1, as in, simultaneous updates for theta_0, theta_1. 