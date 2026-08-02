class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify(arr,n,i):
            largest = i
            l = 2*i+1
            r = 2*i +2

            if l <n and arr[l] > arr[largest]:
                largest = l

            if r <n and arr[r] > arr[largest]:
                largest = r

            if largest !=i:
                arr[largest], arr[i] = arr[i], arr[largest]

                arr = heapify(arr,n,largest)

            return arr

        n = len(nums)
        for i in range(n//2 - 1,-1,-1):
            nums = heapify(nums,n,i)

        for i in range(n-1,0,-1):
            nums[0], nums[i] = nums[i] , nums[0]

            nums = heapify(nums,i,0)


        return nums






