def max_sub_array(k, arr):
    max_sum = 0
    win_sum = 0

    for i in range(len(arr) - k + 1):
        win_sum = 0
        for j in range(i, i+k):
            win_sum += arr[j]
        max_sum = max(max_sum, win_sum)
    return max_sum


def max_sub_array_better(k, arr):
    max_sum = 0
    win_sum = 0
    win_start = 0

    for win_end in range(len(arr)):
        win_sum += arr[win_end]
        if win_end >= k-1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[win_start]
            win_start += 1
    return max_sum


"""
Smallest Subarray with a given sum (easy):
Given an array of positive numbers and a positive number S, 
find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
Return 0, if no such subarray exists.
"""


def smallest_sub(S, arr):
    smallest_len = 100
    win_sum = 0
    win_start = 0
    for win_end in range(len(arr)):
        win_sum += arr[win_end]  # moving forward (expansion of window)
        while win_sum >= S:  # comparison with given S, while important for shrinkage
            win_len = win_end - win_start + 1  # calculation of win length
            smallest_len = min(smallest_len, win_len)  # comparision to best
            win_sum -= arr[win_start]  # sum updation for further use
            win_start += 1  # window shift (shrinkage of window)
        if smallest_len == 1000:
            return 0
    return smallest_len


"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


def kdistinct(str, k):
    max_distinct = 0
    win_start = 0
    char_freq = {}
    for win_end in range(len(str)):
        if str[win_end] not in char_freq:
            char_freq[str[win_end]] = 0
        char_freq[str[win_end]] += 1

        while len(char_freq) > k:
            char_freq[str[win_start]] -= 1
            if char_freq[str[win_start]] == 0:
                del char_freq[str[win_start]]
            win_start += 1
        max_distinct = max(max_distinct, (win_end-win_start+1))
    return max_distinct


"""
Fruits into basket:
Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can't skip a tree. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
"""


def two_basket_collection(arr):
    max_fruits = 0
    win_start = 0
    baskets = {}

    for win_end in range(len(arr)):
        if arr[win_end] not in baskets:
            baskets[arr[win_end]] = 0
        baskets[arr[win_end]] += 1

        while len(baskets) > 2:
            baskets[arr[win_start]] -= 1
            if baskets[arr[win_start]] == 0:
                del baskets[arr[win_start]]
            win_start += 1
        max_fruits = max(max_fruits, (win_end-win_start + 1))
    return max_fruits


"""
Given a string, find the length of the longest substring which has no repeating characters.
"""


def no_repeat_substring(str):
    max_len = 0
    win_start = 0
    sub_str = ''
    dicts = {}

    for win_end in range(len(str)):
        if str[win_end] in dicts:
            win_start = max(win_start, dicts[str[win_end]]+1)
        dicts[str[win_end]] = win_end
        max_len = max(max_len, win_end - win_start + 1)
    return max_len


def main():
    print("Max sum of subarray of K: " +
          str(max_sub_array(3, [2, 1, 5, 1, 3, 2])))
    print("Max sum of subarray of K: " +
          str(max_sub_array(2, [2, 3, 4, 1, 5])))
    print("Max sum of subarray of K: " +
          str(max_sub_array_better(3, [2, 1, 5, 1, 3, 2])))
    print("Max sum of subarray of K: " +
          str(max_sub_array_better(2, [2, 3, 4, 1, 5])))

    print("Smallest subarray length: " +
          str(smallest_sub(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_sub(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_sub(8, [3, 4, 1, 1, 6])))

    print("distinct characters in string with length K: " +
          str(kdistinct("araaci", 2)))
    print("distinct characters in string with length K: " +
          str(kdistinct("araaci", 1)))

    print("maximum number of fruits in a basket: " +
          str(two_basket_collection(['A', 'B', 'C', 'A', 'C'])))
    print("maximum number of fruits in a basket: " +
          str(two_basket_collection(['A', 'B', 'C', 'B', 'B', 'C'])))

    print("length of longest substring is: " +
          str(no_repeat_substring("aabccbb")))
    print("length of longest substring is: " +
          str(no_repeat_substring("abbbb")))


main()
