'''
Given an array of strings strs, write a function that can group the anagrams. The groups should be ordered such that the larger groups come first, with subsequent groups ordered in descending order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input:
strs = ["apt","pat","ear","tap","are","arm"]

Output:
[["apt","pat","tap"],["ear","are"],["arm"]]
Example 2:

Input:
strs = [""]

Output:
[[""]]
Example 3:

Input:
strs = ["a"]

Output:
[["a"]]
Notes:

strs[i] consists of lower-case English letters.
'''


def csGroupAnagrams(strs):
    input_dict = {}
    for i in strs:
        sorted_str = ''.join(sorted(i))
        if sorted_str in input_dict:
            input_dict[sorted_str].append(i)
        else:
            input_dict[sorted_str] = [i]
    return list(input_dict.values())

# O(n)
