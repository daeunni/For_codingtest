"""
Kaden's algorithms 
  - 숫자 array에서 연속된 subset의 최대 합을 구하기 
  - Dynamic Programming의 한 방법
"""

def kaden(nums) :
  globalsum = nums[0]
  localsum = nums[0]

  for i in nums[1:] : 
    localsum = max(i, i+localsum)     # it must be continuous array !!
    globalsum = max(localsum, globalsum)
    
  return globalsum 
