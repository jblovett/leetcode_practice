"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""

from typing import List

def main() -> None:
    input_1 = [-1,0,3,5,9,12]
    target_1 = 9
    target_2 = 12
    print(f"{binary_search(input_1, target_1)}")
    print(f"{binary_search(input_1, target_2)}")
    print(f"{binary_search(input_1, 2)}")
    print(f"{better_binary_search(input_1, target_1)}")
    print(f"{better_binary_search(input_1, target_2)}")
    print(f"{better_binary_search(input_1, 2)}")



# OK but not quite O(log n). More like O(n/2)
def binary_search(input: List[int], target: int) -> int:
    length = len(input)
    j = length // 2
    if length % 2 == 0:
        ##even case
        i = j - 1
    else:
        i = j
    while j < length:
        if input[j] == target:
            return j
        elif input[i] == target:
            return i
        else:
            j += 1
            i -= 1
    return -1

# use an important invariant: array is sorted!
# three index variables. Lower, middle, and Higher.
# check if value at lower, middle, or higher have the target
# if so, return
# if not, then repeat, but change values as follows: 
# do this until L, H, and M have been back to back at most once
    # if target is less than array[middle]
        # higher = middle
        # lower is same
        # middle is ((H - L) // 2), a calculation to find the floored midpoint between higher and lower
    # if target is greater than array[middle]
        # higher is same
        # lower is middle
        # middle ((H - L) // 2)

def better_binary_search(input: List[int], target: int) -> int:
    lower = 0
    higher = len(input) - 1
    middle = ((higher - lower) // 2) + lower
    if input[lower] == target:
        return lower
    elif input[middle] == target:
        return middle
    elif input[higher] == target:
        return higher
    else:
        while lower < (higher - 1):
            middle = ((higher - lower) // 2) + lower
            if input[lower] == target:
                return lower
            elif input[middle] == target:
                return middle
            elif input[higher] == target:
                return higher
            else:
                if target < input[middle]:
                    higher = middle
                else:
                    lower = middle
    return -1

def recursive_binary_search(input: List[int], target: int, higher: int, lower: int) -> int:
    middle = ((higher - lower) // 2) + lower
    if input[lower] == target:
        return lower
    elif input[middle] == target:
        return middle
    elif input[higher] == target:
        return higher
    else:
        if target < input[middle]:
            higher = middle
        else:
            lower = middle
        return recursive_binary_search(input, target, higher, lower)
    return -1
    # lol maybe no haha

#leetcode's answer
def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1




if __name__ == "__main__":
    main()
