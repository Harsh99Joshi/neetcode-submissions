class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution 1 - hashmap
        # TC - O(n^2)
        h = {}
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):
            h[num] = i

        for i in range(n):
            for j in range(i+1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))

        return list(s)