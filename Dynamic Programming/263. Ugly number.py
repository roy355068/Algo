# Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

# Note that 1 is typically treated as an ugly number.

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        # if num contains factors that have factor in [2, 3, 5], I can keep divide it by that number
        # until the num reach 1 or not. If the final num is not 1, means there are other factor that
        # is not one of 2, 3, or 5
	        for i in [2, 3, 5]:
	        	while num % i == 0 < num:
	        		num /= i
	        return num == 1