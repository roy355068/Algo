// Given an array of strings, group anagrams together.

// For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
// Return:

// [
//   ["ate", "eat","tea"],
//   ["nat","tan"],
//   ["bat"]
// ]
// Note: All inputs will be in lower-case.

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList<List<String>>();
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
        	char [] ca = s.toCharArray();
        	Arrays.sort(ca);
        	String temp = String.valueOf(ca);
        	if (!map.containsKey(temp)) {
        		map.put(temp, new ArrayList<String>());
        	}
        	map.get(temp).add(s);
        }
        return new ArrayList<List<String>>(map.values());
    }
}