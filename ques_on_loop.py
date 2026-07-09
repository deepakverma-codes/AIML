# Loop executes a block of code multiple time
nums = [4, 7, 2, 9, 7, 5, 2]

found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print("First duplicate:", nums[i])
            found = True
            break
    if found:
        break

if not found:
    print("No duplicate found")

