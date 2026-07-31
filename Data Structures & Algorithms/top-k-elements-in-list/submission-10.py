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
            max_freq = -1
            for key in dicthash:
                if key not in val and dicthash[key] > max_freq:
                    max_freq = dicthash[key]
                    max_key = key
            val.append(max_key)
        return val

