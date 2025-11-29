class Solution(object):
    def intersection(self, nums1, nums2):
        sets = set(nums1).intersection(set(nums2))
        return list(sets)
