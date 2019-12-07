nums = [int(x) for x in open("numbers.txt").read().strip().split('\n')]
nums_hit = set()
hit_something_twice = False
i = 0
total = 0

while not hit_something_twice:
    total += nums[i % len(nums)]
    if total not in nums_hit:
        nums_hit.add(total)
        i += 1
    else:
        print(total)
        hit_something_twice = True
