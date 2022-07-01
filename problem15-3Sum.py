class Solution:
    def threeSum(self, nums):
        nums.sort()
        #nums = list(dict.fromkeys(nums))
        result = []
        for i in range(len((nums))):
            target =-nums[i];
            left = i + 1
            right = len(nums)-1
            while(left < right):
                sum = nums[right] + nums[left]
                if(sum < target):
                    left +=1
                elif(sum > target):
                    right-=1
                else:
                    a= nums[i],nums[left],nums[right]
                    if a not in result:
                        result.append(a)
                    left +=1
                    right-=1
        return result
