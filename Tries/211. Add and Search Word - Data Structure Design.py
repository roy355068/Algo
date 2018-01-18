class TrieNode(object):
	def __init__(self):
		self.children = {}
		self.isEnd = False

class WordDictionary(object):
	
	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
		node.isEnd = True

	# The word could have . meaning wildcard character
	def search(self, word):
		return self.helper(self.root, 0, word)

	# A helper method for recursively find the word in the Trie
	# node : current node in the trie
	# k : current index in the word
	# word : the target word we would like to find in the Trie
	def helper(self, node, k, word):
		if k == len(word):
			return node.isEnd
		if word[k] != ".":
			return word[k] in node.children and self.helper(node.children[word[k]], k + 1, word)
		else:
			for child in node.children.values():
				if self.helper(child, k + 1, word):
					return True
		return False


