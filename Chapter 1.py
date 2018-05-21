CHAPTER ONE

# Problem 1.3 URLify

# IDEAL
"""
I: Need to replace all spaces in a string with '%20'
D: To replace all spaces in a string with '%20'
E/A: I did not need to use Duke's 7 steps, as I had done this previously by using the .replace built-in function in python.
	 I used my previous knowledge of this function in combination with python's string slicing functionality since one of 
	 the parameters passed was the true length of the string. 
L: From this problem I was able to put my knowledge of different programming languages to use. I was able to analyze the problem
   and choose the programming language that was best suited to solve this problem.
"""
def urlify(user_string, true_length):
	return user_string[:true_length].replace(' ', '%20')


# Problem 1.1 Is Unique

# IDEAL
"""
I: Need to determine if a string contains only unique characters.
D: To see if a string contains only unique characters without using any other data structures.
E/A: I utilized Duke's 7 steps to solve this problem. I created some instances and solved them by hand.
     I wrote down some edge cases as well and decided to handle them by returning False. I tested the cases that
     I came up with and they all passed. My approach for this problem was the one that we had previously discussed
     in the class. I first sorted the string, since all unique characters would be grouped together. 
L: From this problem I learnt how to use previously learnt tricks that we learnt in class to solve this problem.
   By sorting the string first, the time complexity is reduced from O(n^2) to O(n). 
"""

def isUnique(user_string):
	if len(user_string) is 0:
		return False

	if len(user_string) is 1:
		return True

	user_string = sorted(user_string)
	for i in range(len(user_string) - 1):
		if user_string[i] is user_string[i+1]:
			return False

	return True 


# Problem 1.7 Rotate Matrix

# I: Rotate an image 90 degrees.
# D: Figure out a way to rotate an nxn matrix 90 degrees.
# E/A: I used Duke's 7 steps for this problem. When thinking about rotating the image, I was reminded of a problem that I had encountered at work
#	   where I had to rotate a circuit 90 degrees. I utilized this same approach which was to replace the coordinates of the matrix. I utilized a 
#	   geometric approach to rotate coordinates 90 degrees by swapping the x and y values (row and column in matrix) to (-y, x).
# L: From this problem I was able to apply my knowledge of geometry and matrices to rotate it. It was assumed that the matrix needed to be rotated
#    in  a clockwise direction for this solution to be valid. 

def rotate_image_90(matrix):
	rotated_image = matrix
	for i, row in enumerate(matrix):
		for j, col in enumerate(row):
			rotated_image[-j][i] = matrix[i][j]

	return rotated_image

# Problem 1.2

# I: Check if string 2 is a permutation of string 1
# D: Given two strings, need to find a way to check if string 2 is a permutation of string 1. 
# E/A: I used Duke's 7 steps. When solving this problem I thought back to problem 1.1 where we determined if every character in the string was unique.
#      While uniqueness was not necessarily being tested here, a permutation is just a string that is the same length of the original string, but in a different order.
#	   That meant if I sorted both strings and string 2 is a permutation of string 1, then they would be the same.
# L: By sorting the strings, I no longer had to create the permutations myselft and then comparing them with the original string to see if string 2 was in fact a 
#    a permutation of string 1. Sorting the strings also greatly reduced both the time and space complexity of this problem drastically. 

def is_permutation(string1, string2):
	if string1 or string2 is None:
		return False
	string1 = sorted(string1)
	string2 = sorted(string2)
	return string1 == string2


# Problem 1.6 

# I: Implement a method to perform string compression.
# D: Create a method to perform string compression, but if the compression would not be smaller than the orginal string, return the original string. 
# E/A: I used Duke's 7 steps. I didn't recall a problem where I had done this before. Therefore, I relied more on coming up with edge cases and other inputs
#	   in order to test the algorithm. Since every character needs to be checked for compression the time complexity will not be better than O(n)
# L: For this problem I used simple string concatenation and indeces to create the compressed string. 

def string_compression(string):
	if len(string) < 2 or string is None:
		return string
	compressed_string = ''
	count = 1
	curr_char = string[0]
	for i in range(1, len(string)):
		if curr_char == string[i]:
			count += 1

		else:
			compressed_string = compressed_string + curr_char + str(count)
			count = 1
			curr_char = string[i]

	if len(compressed_string) >= len(string):
		return string
	else:
		return compressed_string