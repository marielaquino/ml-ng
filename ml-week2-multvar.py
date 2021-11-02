# Linear Regression with Multiple Variables


'''
MULTIPLE FEATURES 
====================

features x1....xn -> n is num of features, m is num of training examples 
prediction y 

instead of hyp = theta_0 + theta_1*x1....extend that to n amounts of thetas (parameters) and features (x)

hypothesis in inner product of theta matrix transpose and feature matrix for multivariate LR 


========================
GRAD DESCENT FOR MVLR
========================

for n >= 1 features:

theta_j := theta_j - alpha* (1/m) * sum from i -> m (h_theta*xi - yi)xi_j 
