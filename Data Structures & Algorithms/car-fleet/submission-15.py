class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))
        s = []
        
        for p,v in pairs:
            s.append((target - p)/v)
            
        fleet = 0
        prev = 0
        while s:
            a = s.pop()
            if a > prev:
                prev = a
                fleet+=1
        return fleet


