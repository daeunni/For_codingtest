"""
Maximum Sum Circular Subarray
  - Circular array(순환 array)가 주어질 때, 여기서 연속된 subset의 maxsum을 구하는 문제
  - Kadane's algorithm을 이용한다. 
"""

def maxSubarraySumCircular(nums: List[int]) -> int:
    # Kadane's algorithms
    def kk(nums):
        globalsum = nums[0]
        localsum = nums[0]

        for i in nums[1:] : 
            localsum = max(i, i+localsum)     # it must be continuous array !!
            globalsum = max(localsum, globalsum)
        return globalsum 

    # Kadane's algorithms > min 
    def kk_min(nums):
        globalsum = nums[0]
        localsum = nums[0]

        for i in nums[1:] : 
            localsum = min(i, i+localsum)     # it must be continuous array !!
            globalsum = min(localsum, globalsum)
        return globalsum 

    minsum = kk_min(nums)
    maxsum = kk(nums)
    
    # If minSum == sum return maxSum, otherwise return max(maxSum, sum - minSum). >> 이 이유를 잘 모르겠음. 
    if minsum == sum(nums) : 
        return maxsum
    else : 
        return max(maxsum, sum(nums) - minsum)
