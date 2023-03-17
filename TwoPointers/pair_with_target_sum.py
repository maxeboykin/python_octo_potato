print("-------------------------------------------------------")
print("Pair With Target Sum")
input = [1, 2, 3, 4, 6];
target = 6;
print(f'input array:  [{input}] and target: {target}')
print("----------------------")


def pair_with_target_sum(inputArr, targetSum):
    left = 0
    right = len(inputArr) - 1
    while left < right:
        curSum = inputArr[left] + inputArr[right]
        if curSum == targetSum:
            return [left, right]
        elif curSum < targetSum:
            left += 1
        elif curSum > targetSum:
            right -= 1

    return [-1, -1]


print(pair_with_target_sum(input, target))
