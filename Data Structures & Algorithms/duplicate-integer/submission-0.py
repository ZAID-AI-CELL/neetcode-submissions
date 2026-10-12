class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vus = set()
        for n in nums:
            if n in vus:
                return True
            vus.add(n)
        return False