class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) TC
        h = {}
        t = target
        for i in range(len(nums)):
            if (t-nums[i]) in h:
                return [h[t-nums[i]], i]
            else:
                h[nums[i]] = i

        
        
        # # brute force - 2 for loops
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        