# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

# The idea is using a dictionary (HashMap) to store the 
# height : [k-value, original position in array] as key : value pair in the dict
# and store the height of every person.
# Sort the height with descending order and start dealing with the highest value

# Bcuz the highest value could only have a > 0 k-value when there's someone has the same height
# standing before him/her, so the k-value of the highest person is their relative position in
# the new array.
# For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
        	return []
        dic, height, res = {}, [], []
        for i in xrange(len(people)):
        	p = people[i]
        	dic.setdefault(p[0], []).append([p[1], i])
        	if p[0] not in height:
        		height.append(p[0])
        height.sort(reverse = True)
        for h in height:
        	dic[h].sort()
        	for p in dic[h]:
        		res.insert(p[0], people[p[1]])
        return res

