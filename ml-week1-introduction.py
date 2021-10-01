# WEEK 1 - Introduction

""" 

WHAT IS MACHING LEARNING 

A computer program is said to learn from experience E with respect to some task T and some performance measure P if its performance on T as measured by P improves after some experience E.


# Supervised Learning - teach the computer explicitly
# Unsupervised Learning - allow the computer to learn by itself 

# -> Learning applied machine learning in this course, was missing in UC Berkeley course. There is a difference between people who do and do not understand how to apply the algorithms/tools.


"""



""" 
WHAT IS SUPERVISED LEARING 

*** House Price Prediction Example ***
we have a bunch of points that are houses (x axis, square ft & y axis house price) and can fit linear or quadratic function, for example. 

	SUPERVISED -> giving the model the "right answers" off the bat. for each house, what is the "right" or "actual" price the house sold for. 
	REGRESSION -> predict continuous valued output. (price) 

*** Breast Cancer Prediction ***
Given tumour size, what is probability of being malignant/benign? 

	CLASSIFICATION -> predict discrete value output
			Given tumour size AND age, what is probability of malignancy/benignness? 
			-> Fit a straight line? (linear separability) 

	You can have infinite features/attributes to predict outcomes. 
		-> HOW DO YOU DEAL WITH THESE? 

	SVMs have a mathematical trick that allows for this. There's an algorithm for it! 

"""

""" 
WHAT IS UNSUPERVISED LEARING 

Given a dataset, we're not told a "right value." "Hi model, can you find some sort of structure or pattern with this?"

1. Clustering Algorithms
	-> Google News
		Looks at news stories, groups them into similar stories and presents them together on webpage. 

	-> Organize Computer Clusters (group computers that work together to run more efficiently)
	-> Social Network Analysis (cohesive groups of friends)
	-> Market Segmentation (customer information, automatically find groups of customers)
	-> Astronomical Data Analysis (galaxy formation patterns)

2. Cocktail Party Problem
	N people talking at the same time with overlapping voices. 

	N = 2, we put up two microphones at different points in the room that captures different combo of overlapping speakers voices. 

	ALGORITHM -> Single Value Decomposition, in this case, applied to audio source separation 


Using Octave to streamline process & get prototypes off the ground. 
"""








