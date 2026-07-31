class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicthash = {}
       
        for num in nums:
            if num in dicthash:
                dicthash[num] += 1
            else:
                dicthash[num] =1
        
        val = []
        for _ in range(k):
            max_key = max(dicthash, key=lambda x: dicthash[x] if x not in val else -1)
            val.append(max_key)
        return val
