class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        use a sliding window
        have a dictionary that counts the occurences of a character in the current sliding window
        if any if the the character is found in the sliding window with occurences > 1, shift the left pointer until every occurences is <= 1
        """

        left = 0
        counter = {}
        longest_substring = 0
        for right in range(len(s)):
            curr = s[right]
            counter[curr] = counter.get(curr, 0) + 1
            # while there are two of the same character in our sliding window, shift the left pointer and delete values from our hashmap until there's only one of each character
            # only character we can get two of is curr
            while counter[curr] > 1:
                left_character = s[left]
                counter[left_character] -= 1
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        
        return longest_substring