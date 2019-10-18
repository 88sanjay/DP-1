"""
Approach : There are 3 possible cases for a successful heist. Consider an array nums = [a1,a2,a3,a4 ..] 
rob(nums) = max (rob(nums[1:]) if no robbery occurs at a1 , a1 + rob(nums[2:]) if robbery occurs at a1 and a3 next, 
a1 + rob(nums[3:]) if robbery occurs at a1 and a4 next)

Time complexity : O(n)
Space complexity : O(n) because we use a cache

Works on leet code
"""
class Solution(object):
    
    solutions = {}
    
    def helper(self,nums,start_idx) : 
        """
        Returns the start of the maximal heist array and returns to value of the heist
        """
        if start_idx == None :
            return None, 0
        
        if self.solutions.get(start_idx) :
            return self.solutions[start_idx]
        
        
        if len(nums) - start_idx == 0 :
            return None, 0

        return_idx = None
        heist_total = None

        if len(nums) - start_idx == 1 :
            self.solutions[start_idx] = (start_idx,nums[start_idx])
            return_idx,heist_total = start_idx, nums[start_idx]
        elif len(nums) - start_idx == 2 :
            if nums[start_idx] > nums[start_idx + 1] :
                return_idx,heist_total = start_idx,nums[start_idx]
            else :
                return_idx,heist_total = start_idx+1,nums[start_idx+1]        
        elif len(nums) - start_idx == 3 :
            if (nums[start_idx] + nums[start_idx+2]) > nums[start_idx + 1] :
                return_idx,heist_total = start_idx,(nums[start_idx]+nums[start_idx+2])
            else :
                return_idx,heist_total = (start_idx+1),nums[start_idx+1]
        else : # array is greater than size 3 
            r1 = self.helper(nums, start_idx +1)
            r2 = self.helper(nums, start_idx +2)
            r3 = self.helper(nums, start_idx +3)
            
            valid_cases = []
            if (r1[0] != None) and (r1[0] == start_idx +1) :
                valid_cases.append(r1)
            
            if (r2[0] != None) and (r2[0] == start_idx +2) :
                valid_cases.append((start_idx, nums[start_idx] + r2[1]))

            if (r3[0] != None) and (r3[0] == start_idx +3) :
                valid_cases.append((start_idx, nums[start_idx] + r3[1]))
            
            valid_cases.sort(key = lambda x : x[1],reverse = True)
            return_idx, heist_total = valid_cases[0][0], valid_cases[0][1]

                            
        self.solutions[start_idx] = (return_idx,heist_total)
        return (return_idx, heist_total) 
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.solutions = {}
        return self.helper(nums,0)[1]
        
