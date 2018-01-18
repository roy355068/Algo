class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 1
        l = len(s)
        # Use three nested loops to define the borders of those 4 substrings
        while i < 4 and i < l - 2:
        	j = i + 1
        	while j < i + 4 and j < l - 1:
        		k = j + 1
        		while k < j + 4 and k < l:
        			s1 = s[:i]
        			s2 = s[i:j]
        			s3 = s[j:k]
        			s4 = s[k:]
        			if self.valid(s1) and self.valid(s2) and self.valid(s3) and self.valid(s4):
        				res.append(s1 + "." + s2 + "." + s3 + "." + s4)
        			k += 1
        		j += 1
        	i += 1
       	return res

    # if length of s is greater than 3 or equal to 0
    # or there's leading zero
    # or the string's integer value is greater than 255
    # return False => indicates the substring is invalid
    def valid(self, s):
    	if len(s) > 3 or not s or (s[0] == "0" and len(s) > 1) or int(s) > 255:
    		return False
    	return True