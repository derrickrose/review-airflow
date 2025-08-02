# introduction
## arrays and strings are 2 of the most fundamental data structures
## and very similar when it comes to solving problems as they are both ordered and can be iterated over

# resizing an array
## technically an array cannot be resized
## a dynamic array or list can be
## in the context of DSA, when they talk about array, they are referring to dynamic array
## in this course we will use the term array to refer to a list (resizable)

# mutability
## similarly strings are immutable in java and python
## in c++ they are
arr = [1, 2, 3]
arr[0] = 10
print(arr)  # mutable
s = "abc"
print(s)
## s[0] = "d" # TypeError cannot accept item assignment
## we have to recreate the all string as such from scratch
s = "abd"
print(s)  # the thing is if the length of s is 100000 characters it is expensive since the modification is O(n)

# time complexity of array (list) (mutable)
## appending to the end O(1) (amortized O(1)) https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1
## popping from end O(1)
## insertion not from end O(n)
## deletion not from end O(n)
## modifying an element O(1)
## random access O(1)
## checking if element exists O(n)

# time complexity of a string (immutable)
## appending to the end O(n)
## popping from end O(n)
## insertion not from end O(n)
## deletion not from end O(n)
## modifying an element O(n)
## random access O(1)
## checking if element exists O(n)

# two pointers
## https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/
## let's say we have a list
## at the beginning the pointer left at position 0, the right one at position len()-1
## the strength of this technique is that we will never have more than O(n) iterations
## since the pointers start n-away from each other and move at least one step closer in every iteration.
## therefore if we can keep the work inside each iteration at O(1), this technique will result in a linear runtime (usually the best)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fun(arr):
    left = 0
    right = len(
        arr) - 1  # while left <= right:  # Do some logic here depending on the problem  # Decide what to do  # 1 left++  # 2 right--  # 3 both : left++ and right--


# example
## check a palindrome
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


val = "abcba"
print(is_palindrome(val))
val = "abc"
print(is_palindrome(val))


# check almost like Two Sum but for sorted list
## brute force O(n^2)
def check(nums, t):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == t:
                print(nums[i], "+", nums[j], "=", t)
                print("i", i, "j", j)
                return True

    return False


## since the array is sorted, we can implement two pointers from both extremities
## double pointer O(n) since the maximum will be n
## space complexity O(1) since we just use a var
def check(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] + nums[right] == target:
            print(nums[left], "+", nums[right], "=", target)
            print("left", left, "right", right)
            return True
        left += 1
        right -= 1
    return False


nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(check(nums, target))

# check let's say two sum but array is not sorted
nums = [15, 1, 9, 4, 8, 6, 14, 2]


## pas besoin de montrer index des éléments
def check(nums, target):
    s = set()
    for index in range(len(nums)):
        if target - nums[index] in s:
            return True
        else:
            s.add(nums[index])
    return False


print("using set", check(nums, 13))


## si on a besoin de montrer l'index des éléments
def check(nums, target):
    dico = {}
    for index in range(len(nums)):
        if target - nums[index] in dico:
            print("i", dico[target - nums[index]], "j", index)
            return True
        else:
            dico[nums[index]] = index
    return False


print("using dico", check(nums, 13))
# next Another way to use two pointers
# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/