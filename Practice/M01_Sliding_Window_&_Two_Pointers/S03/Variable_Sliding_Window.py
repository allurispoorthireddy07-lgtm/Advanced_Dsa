from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    min_len = float("inf")
    curr_sum = 0

    for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
    return min_len if min_len != float("inf") else 0
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))  # Output: 2