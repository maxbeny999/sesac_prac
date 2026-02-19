n = 30
lists = []
perfect_num = []
for nums in range(1, n + 1):
    if nums % nums == 0:
        lists.append(nums)
        print(lists)
    if sum(lists[:-1]) == n:
        perfect_num.append(n)
print(perfect_num)
