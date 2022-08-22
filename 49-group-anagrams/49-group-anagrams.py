class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for str in strs:
            count_letters = [0] * 26
            
            for ch in str:
                count_letters[ord(ch) - ord('a')] += 1
            
            result[tuple(count_letters)].append(str)
            
        return result.values()