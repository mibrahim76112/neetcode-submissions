class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if i > 0:
                s.append(i)
            #    print(s)
            else:
                while s and s[-1] > 0 and abs(s[-1]) < abs(i):
                    s.pop()
                
                if not s or s[-1] < 0:
                    s.append(i)
                elif abs(s[-1]) == abs(i):
                    s.pop()
             
              #  print(s)
        return s

