class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we're trying to find the longest substring without unique characters
        # best solution is however many ascii characters there are
        # we can have a sliding window that counts the unique values with the size of a set/dict
        # every time a unique ascii is found, we have a key value pair (ascii, index) to the dict
        # if we encounter a value that is reoccuring, we keep the number the same, and move the left pointer up to the index after the value to the ascii
        # have a max integer that keeps track of the max unique values in a substring

        # p w w k e w
        # d: (p, 0), (w, 1)
        # max = 2

        d = {}
        max_value, curr_unique = 0, 0
        left, right = 0, 0
        while right < len(s):
            curr = s[right]
            if curr not in d or d[curr] < left:
                d[curr] = right
                curr_unique += 1
            else:
                curr_unique -= (d[curr] - left)
                left = d[curr] + 1
                d[curr] = right

            if curr_unique > max_value:
                max_value = curr_unique

            right += 1

        return max_value
        
