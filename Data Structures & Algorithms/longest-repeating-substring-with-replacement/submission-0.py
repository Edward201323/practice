class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what is the length of the longest substring of one character
        # what if we get k replacements?

        """
        I'm going to break down the problem into a simpler version with pseudocode
        left = 0, max = 1
        for right in range(1, len(s)):
            if char at right pointer != char at left pointer:
                set left = right
            max = max(max, right - left + 1)
        return max

        accounting for k replacements, we could add another pointer so that we go back to the first unique replacement rather than back to the right pointer, and make it so that we have k amount of leeway. but what if all characters are different? this will cause an n^2 Solution

        how could we utilize another data structure to help us get the solution?

        we can use a dictionary to count the frequency of each character in the window
        window length <= most freq character + k
        window length - k <= most freq character
        
        slide our window to the elft
        throughout this process, we have to keep track of the biggest window
        """

        left = 0
        max_window = 0
        counter = {}
        for right in range(len(s)):
            curr = s[right]
            counter[curr] = counter.get(curr, 0) + 1
            most_freq = max(counter.values()) # O(1) because we can only have at max 26 values

            # whenever most freq character != window length - k
            # window length - k > most freq character
            while (right - left + 1) - k > most_freq:
                counter[s[left]] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)



        return max_window







        
