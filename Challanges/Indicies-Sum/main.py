from itertools import combinations
nums = [1,2,3,6,7,5]
target = 13

pairs = list(combinations(nums, 2))
print(pairs)

for num in pairs:
    if sum(num) == target:
        stored_num = num
        print(nums.index(stored_num[0]))
        print(nums.index(stored_num[1]))
