'''
Given a pattern and a string a, find if a follows the same pattern.

Here, to "follow" means a full match, such that there is a one-to-one correspondence between a letter in pattern and a non-empty word in a.

Example 1:

Input:
pattern = "abba"
a = "lambda school school lambda"

Output: true
Example 2:

Input:
pattern = "abba"
a = "lambda school school coding"

Output:
false
Example 3:

Input:
pattern = "aaaa"
a = "lambda school school lambda"

Output: false
Example 4:

Input:
pattern = "abba"
a = "lambda lambda lambda lambda"

Output: false
Notes:

pattern contains only lower-case English letters.
'a' contains only lower-case English letters and spaces ' '.
'a' does not contain any leading or trailing spaces.
All the words in a are separated by a single space.
'''


def csWordPattern(pattern, a):
    patt_dict = {}
    # Must split the words within our string into individual tokens
    loopstr = a.split()

    if len(pattern) != len(loopstr):
        return False

    for i, token in enumerate(loopstr):

        if token in patt_dict.values():
            pass

        elif pattern[i] not in patt_dict:
            patt_dict[pattern[i]] = token

        if patt_dict.get(pattern[i]) != token:
            return False

    return True

# O(n)
