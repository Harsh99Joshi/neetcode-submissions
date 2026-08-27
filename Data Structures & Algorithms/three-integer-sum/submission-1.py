class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #solution 2 - sort input. fix i and use 2 pointers on the rest of the array
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue  # restart and skip current i if it is the same value as before
            
            lo, hi = i+1, n-1
            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo+1, hi-1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo<hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif summ > 0:
                    hi -= 1
                else:
                    lo += 1
        return ans
        # solution 1 - hashmap
        # TC - O(n^2)
        # h = {}
        # n = len(nums)
        # s = set()

        # for i, num in enumerate(nums):
        #     h[num] = i

        # for i in range(n):
        #     for j in range(i+1, n):
        #         desired = -nums[i] - nums[j]
        #         if desired in h and h[desired] != i and h[desired] != j:
        #             s.add(tuple(sorted([nums[i], nums[j], desired])))

        # return list(s)