import json

print('-------------------------------------------------------')
print('triple sum to zero')
input = [0, 0, 1, 1, 2, 6]
input2 = [1, 0, 1, 1]
target = 5
print(f'Given an array of unsorted numbers and a target number, find a triplet in the array whose target is as close '
      f'to the target number as possible. Return the sum of the triplet. If there are both numbers that are tied to '
      f'be close choose the one with a lower sum: Input unsorted array: [{input}] and target: {target}.')


# sort the array so its easier to find duplicates its not like binary search since we are moving the pointers
# incrementally or decrementally by 1 not saying left = mid + 1 etc
# sorting the array is O (n * logN) and we are searching the entire array for two sum to zero for each
# n so that would be n^2. so for time its O(nlogn) + n^2 which is just n^2 and that is way better than n^3
# space complexity would be O(n)

def triple_sum_close_to_target(arr, target):
    arr.sort()  # n(log(n))
    print(json.dumps(arr))
    smallest_difference = float('inf')
    triples_sum = float('inf')
    temp_sum = 0
    for i in range(0, len(arr) - 2, 1):
        [smallest_difference, temp_sum] = _two_sum_close_to_target(arr, arr[i], i + 1, smallest_difference, target, triples_sum)
        triples_sum = min(temp_sum, triples_sum)

    return triples_sum


# tricky logic in second half of if statement to see if when we are even in difference
#           if the currentSum is less than target as opposed to greater than target
#           if its less than target than the curDelta should be positive and thus bigger
#           than the negative smallest_difference counterpart

def _two_sum_close_to_target(arr, first, start_idx, smallest_difference, target, triples_sum):
    right = len(arr) - 1
    left = start_idx
    while left < right:
        current_sum = arr[left] + arr[right] + first
        cur_delta = target - current_sum
        if cur_delta == 0:
            return cur_delta
        if abs(cur_delta) < abs(smallest_difference) or \
                (abs(cur_delta) == abs(smallest_difference) and cur_delta > smallest_difference):
            smallest_difference = cur_delta
            triples_sum = current_sum

        if cur_delta > 0:
            left += 1
        else:
            right -= 1

    return [smallest_difference, triples_sum]


print(triple_sum_close_to_target(input, target))
