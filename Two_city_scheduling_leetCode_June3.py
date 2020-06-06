class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff = []
        total = 0
        for i,j in costs:
            diff.append(i-j)
            total = total+i
            
        diff = sorted(diff)
        
        for k in range(len(costs)//2,len(costs)):
            total = total-diff[k]
        return total    
