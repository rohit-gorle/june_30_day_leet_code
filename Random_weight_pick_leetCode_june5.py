class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cdf = [0]
        for weight in w:
            self.cdf.append(self.cdf[-1] + weight)

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random.randint(1, self.cdf[-1])
        idx = bisect.bisect_left(self.cdf, rand)
        return idx-1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
