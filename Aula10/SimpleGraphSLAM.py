# adapted from Sebastian Thrun, Programming a Robotic Car, udacity

# -----------
# User Instructions
#
# Write a function, doit, that takes as its input an
# initial robot position, move1, and move2. This
# function should compute the Omega and Xi matrices
# discussed in lecture and should RETURN the mu vector
# (which is the product of Omega.inverse() and Xi).
#
# Please enter your code at the bottom.


 
from math import *
from matrix import matrix
import random


#===============================================================
#
# SLAM in a rectolinear world (we avoid non-linearities)
#	  
# 
#===============================================================



# ######################################################################
# ######################################################################
# ######################################################################


"""
For the following example, you would call doit(-3, 5, 3):
3 robot positions
  initially: -3
  moves by 5
  moves by 3

  

which should return a mu of:
[[-3.0],
 [2.0],
 [5.0]]
"""
def doit(initial_pos, move1, move2):
	#
	#
	# Add your code here.
	#
	#
	
	return mu

doit(-3, 5, 3)



