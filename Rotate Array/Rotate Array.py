class Solution(object):
    def rotate(self, nums, k):
        var = len(nums)
        k = k % var
        nums[:] = nums[var-k:] + nums[:var-k]
