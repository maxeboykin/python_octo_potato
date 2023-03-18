print("-------------------------------------------------------")
print("Dutch National Flag")
input = [1, 1, 1, 0, 2, 1, 0]

print(f'Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, '
      f'hence, we can’t count 0s, 1s, and 2s to recreate the array.   Input: [{input}], The flag of the Netherlands '
      f'consists of three colors: red, white and blue; and since our input array also consists of three different '
      f'numbers that is why it is called Dutch National Flag problem.')
print("----------------------")
# // you need a third pointer here
# // draw it out in a binder
# // the left should be pointing to always the next number to a bunch of 0s
# // the right should be pointing to the always the next number next to a bunch of 2s
# // i should be the one swapping with left and right
# // would be O(n) time and O(1) space


def dutch_national_flag(arr):
    left = 0
    right = len(arr) - 1
    i = 0
    while i < right:
        if arr[i] == 0:
            _swap(arr, i, left)
            left += 1
        elif arr[i] == 1:
            i += 1
        else:
            _swap(arr, i, right)
            right -= 1

    return arr


def _swap(arr, x, y):
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp



print(dutch_national_flag(input))
