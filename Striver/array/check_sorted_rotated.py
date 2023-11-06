def check(nums) -> bool:
        n = len(nums)
        count=0
        for i in range(1,n):
            if (nums[i-1] > nums[i]):
                count+=1
        if(nums[n-1] > nums[0]):
            count+=1
        return count<=1

nums = [3,4,5,1,2]
res = check(nums)
print(res)