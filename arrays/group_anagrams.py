# O(m * nlogn) solution
class Solution(object):
    from collections import defaultdict

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)

        for s in strs:
            sorted_s = str(sorted(s))
            hashmap[sorted_s].append(s)

        result_list = []
        for ls in hashmap.values():
            result_list.append(ls)
        
        return result_list
            
# O(m * n) solution
class Solution(object):
    from collections import defaultdict

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)

        # Develop ordered alphabet list
        
        for s in strs:
            ascii_list = [0] * 26
            for char in s:
                ascii_list[ord(char) - ord('a')] += 1
            hashmap[tuple(ascii_list)].append(s)

        result_list = []
        for ls in hashmap.values():
            result_list.append(ls)
        
        return result_list