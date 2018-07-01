#encoding:

def nextPermutation(nums):
    length = len(nums)
    for i in range(length-1, 0, -1):
        if nums[i] > nums[i-1]:
            return nums[:i-1] + [nums[i], nums[i-1]] + nums[i+1:]
    return nums[::-1]

if __name__ == '__main__':
    print nextPermutation([1, 2, 3])
    print nextPermutation([3, 2, 1])
    print nextPermutation([1, 1, 5])
    print nextPermutation([1, 2])
    print nextPermutation([1])