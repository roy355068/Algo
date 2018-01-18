# You want to buy public transport tickets for the upcoming month.
# You know exactly the days on which you will be travelling.
# The month has 30 days and there are three types of ticket:

# 1-day ticket, costs 2, valid for one day;
# 7-day ticket, costs 7, valid for seven consecutive days (e.g. if the first valid day is X, then the last valid day is X+6);
# 30-day ticket, costs 25, valid for all thirty days of the month.
# You want to pay as little as possible.

# You are given a sorted (in increasing order) array A of dates when you will be travelling. For example, given:

# A[0] = 1
# A[1] = 2
# A[2] = 4
# A[3] = 5
# A[4] = 7
# A[5] = 29
# A[6] = 30

# You can buy one 7-day ticket and two 1-day tickets. The two 1-day tickets should be used on days 29 and 30.
# The 7-day ticket should be used on the first seven days of the month.
# The total cost is 11 and there is no possible way of paying less.

# Write a function:

# class Solution { public int solution(int[] a); }

# that, given a zero-indexed array A consisting of N integers that specifies days on which you will be traveling, returns the minimum amount of money that you have to spend on tickets for the month.

# For example, given the above data, the function should return 11, as explained above.

# Assume that:
# -N is an integer within the range [0..30];

# -each element of array A is an integer within the range [1..30];

# -array A is sorted in increasing order;

# -the elements of A are all distinct.

def solution(a):
	last = a[len(a) - 1]
	cost = [0 for _ in xrange(last + 1)]
	for i in xrange(last + 1):
		if i in a:
			if i - 1 < 0:
				continue
			elif i - 7 < 0:
				cost[i] = cost[i - 1] + 2
			elif i - 30 < 0:
				cost[i] = min(cost[i - 1] + 2, cost[i - 7] + 7)
			else:
				cost[i] = min(cost[i - 1] + 2, cost[i - 7] + 7, cost[i - 30] + 25)
		else:
			cost[i] = cost[i - 1]
	return cost[last]

print solution([1,2,4,5,7,29,30])
print solution([1,2,4,5,7,11, 13,15,16,17,18, 29, 30])
print solution([1,2,4,5,7,11,12,13,14,15,16,17,21,22,23,24,25,29,30])
