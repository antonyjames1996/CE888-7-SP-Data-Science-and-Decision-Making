# Write a function list_to_array that receives a list as a function and returns the list converted into a numpy array

import numpy as np

def list_to_array(myList):
    return np.array(myList)
    ## Your code goes here
    

# Using numpy, write a function called 'median', which takes an array or list of numbers as input and calculates their median.

import numpy as np

def median(numbers):
    return np.median(numbers)
    ## Your code goes here
    
    
# Using numpy, write a function called 'percentile', which takes as input an array or list of numbers and a number between 0-100 (the percentile that the user wants to calculate) and returns the percentile.

import numpy as np

def percentile(numbers, perc):
    return np.percentile(numbers, perc)
    ## Your code goes here
    
    
# Using numpy, write a function called 'sorting_choice', which takes as input an array or list of numbers and a string (which should be either 'asc' or 'desc' for ascending/descending) and returns the same numbers sorted in ascending/descending order. The default value if no string is provided should be 'asc'.

import numpy as np

def sorting_choice(myArray, order=''):
    sorted_arr = np.sort(myArray)
    if  order == 'desc':
        return sorted_arr[::-1]
    return sorted_arr
    ## Your code goes here
    
    
# Using numpy, write a function called 'stdev_of_array_columns', which takes as input a 2D array of numbers and returns the column-wise standard deviations of the array.

import numpy as np

def stdev_of_array_columns(numbers):
    return np.std(numbers, axis=0)
    ## Your code goes here
    

# Using numpy, write a function called 'percentile_array_columns', which takes as input a 2D array of numbers and a percentile (number between 0-100) and returns the column-wise percentiles of the array.

import numpy as np

def percentile_array_columns(myArray, perc):
    return np.percentile(myArray, perc, axis = 0)
    ## Your code goes here
    
# We're going to use numpy to generate random numbers. Check the documentation for numpy.random.choice() to complete the functions below.

# NOTE: it's important that you pass the parameters to np.random.choice in order. For example, if the instructions say 'return A with probability A1 and B with probability B1', you should pass the arguments to np.random.choice as np.random.choice([A, B], p=[A1, B1]) to be marked correctly.

import numpy as np

# Define our actions

def action_0():
    ''' This should return 1 with probability 50%, and 0 with probability 50%'''
    ## Your code here
    return np.random.choice([1, 0], p=[0.5, 0.5]) 


def action_1():
    ''' This should return 1 with probability 60%, and 0 with probability 40%'''
    ## Your code here
    return np.random.choice([1, 0], p=[0.6, 0.4])


def action_2():
    ''' This should return 1 with probability 20%, and 0 with probability 80%'''
    ## Your code here
    return np.random.choice([1, 0], p=[0.2, 0.8])


# We're going to use numpy to generate random numbers. Check the documentation for numpy.random.choice() to complete the functions below.

# NOTE: it's important that you pass the parameters to np.random.choice in order. For example, if the instructions say 'return A with probability A1 and B with probability B1', you should pass the arguments to np.random.choice as np.random.choice([A, B], p=[A1, B1]) to be marked correctly.

import numpy as np

# Define our actions

def policy():
    return np.random.choice([0, 1, 2], p=[0.3333333333, 0.333333333, 0.333333333333])
    ''' This should return 0, 1, or 2 with equal probabilities '''
    ## Your code here

# We're going to use numpy to generate random numbers. Check the documentation for numpy.random.choice() to complete the functions below.

# NOTE: it's important that you pass the parameters to np.random.choice in order. For example, if the instructions say 'return A with probability A1 and B with probability B1', you should pass the arguments to np.random.choice as np.random.choice([A, B], p=[A1, B1]) to be marked correctly.

import numpy as np


def policy(p1, p2, p3, p4=0.5):
    # p1, p2, p3 are, respectively, the probabilities of choosing between 1, 2, and 3
    # the default value for p4 should be 0.5
    # action equals 1 with probability p1, 2 with probability p2, and 3 with probability p3
    action = np.random.choice([1,2,3], p=[p1, p2, p3]) # Your code here
    # Depending on the value of 'action', we choose one of the following options:
    # if action is 1: return action1()
    # if action is 2: return action2()
    # if action is 3: return action1() with probability p4, and action2() otherwise
    if action == 1:
        return action1()
    if action == 2:
        return action2()
    if action == 3:
        return np.random.choice([action1(), action2()], p=[p4, 1-p4])
    ## YOUR CODE HERE



def action1(p=0.2):
    # Return 0 with probability p and 1 otherwise
    # the default value for p should be 0.2
    return np.random.choice([0, 1], p=[p, 1-p])
    ## YOUR CODE HERE
    

def action2(p=0.9):
    # Return 3 with probability p and -5 otherwise
    # the default value for p should be 0.9
    return np.random.choice([3, -5], p=[p, 1-p])
    ## YOUR CODE HERE




