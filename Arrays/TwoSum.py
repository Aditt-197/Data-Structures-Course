def twoSum(nums, target):
    index = []

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                index.append(i)
                index.append(j)
                return index

x = [2, 7, 11, 15]
y = 9
print(twoSum(x, y))