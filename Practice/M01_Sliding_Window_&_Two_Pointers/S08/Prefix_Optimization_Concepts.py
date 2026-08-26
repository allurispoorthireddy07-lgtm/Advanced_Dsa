'''
input: nums = [1,2,3,4]
output: [1,3,6,10]
'''
'''using Brute Force'''
def prefix_sum_brute_force(nums):
    prefix_sum = []
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i + 1):
            current_sum += nums[j]
        prefix_sum.append(current_sum)
    return prefix_sum

'''using Prefix Sum Optimization'''
def prefix_sum_optimized(nums):
    prefix_sum = []
    current_sum = 0
    for num in nums:
        current_sum += num
        prefix_sum.append(current_sum)
    return prefix_sum

'''using traditional way'''
nums = [1,2,3,4]
res=[0]*(len(nums))
for i in range(len(nums)):
    curr_sum = 0
    for j in range(0,i+1):
        curr_sum += nums[j]
    res[i] = curr_sum
print(res)        

'''optimal sol'''
nums = [1,2,3,4]
for i in range(1,len(nums)):
    nums[i] = nums[i-1]+nums[i]
print(nums)    


'''leetcode:
1732
1991
724
2574'''

'''
724
523
1652
1248
1763

'''