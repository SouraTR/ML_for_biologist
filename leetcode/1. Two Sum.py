def twoSum(nums, target):
    d = dict(enumerate(nums))
    d = {v: k for k, v in d.items()}
    for i in range(len(nums)):
        remainder = target-nums[i]
        try:
            if i!=d[remainder]:
                return([i, d[remainder]])
        except KeyError:
            continue
    
        
print(twoSum([3,2,4], 6))

# print(list(enumerate([3,2,4])))
# # def twoSum(nums, target):
# #     d = {}
# #     for i, j in enumerate(nums):
# #         r = target - j
# #         if r in d:
# #             return [d[r], i]
# #         d[j] = i

# # print(twoSum([3,2,4], 6))
