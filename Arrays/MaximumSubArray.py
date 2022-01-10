def maxSubArray(nums):
    currentSum = 0
    total = 0
    #iterate through the array
    for i in range(len(nums)):

        currentSum += nums[i]
        total = max(total, currentSum)

        if currentSum < 0:
            currentSum = 0

    return total