class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashmap = defaultdict(int)
        
        for n in nums:
            hashmap[n] += 1
        
        ans_count = sorted(hashmap.values(), reverse = True)[:k:]
        
        for c in ans_count:
            for x in hashmap.keys():
                if hashmap[x] == c  and x not in ans:
                    ans.append(x)
                    break
        
        return ans