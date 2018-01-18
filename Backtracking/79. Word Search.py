class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in xrange(len(board)):
        	for j in xrange(len(board[0])):
        		if self.helper(board, word, i, j, 0):
        			return True
        return False
    
    def helper(self, board, word, i, j, curr):
    	if curr == len(word):
    		return True
    	if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[curr] != board[i][j]:
    		return False
    	
    	board[i][j] = "*"
    	curr += 1
    	res = self.helper(board, word, i + 1, j, curr) or self.helper(board, word, i - 1, j, curr) \
    			or self.helper(board, word, i, j + 1, curr) or self.helper(board, word, i, j - 1, curr) 
    	board[i][j] = word[curr - 1]

    	return res