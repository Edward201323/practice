class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        If I were asked if s1 and s2 are permutations of eachother, I create two dictionarys that counts occuerneces in each individual string, and compare the dictionaries and see if they were equal.
        
        d1 = Coutner(s1)
        left = 0
        d2 = Counter(sliding window)
        for right in range s2:
            s2[right] = curr
            d2[curr] += 1
            
            if d1 == d2:
                return True

            while d2[curr] > d1[curr] and left < right:
                adjust sliding window
                adjust d2 accordingly

        return False
    
        """

        counter1 = {}
        for c in s1:
            counter1[c] = counter1.get(c, 0) + 1

        left = 0
        counter2 = {}
        for right in range(len(s2)):
            curr = s2[right]
            counter2[curr] = counter2.get(curr, 0) + 1
            
            while counter2.get(curr, 0) > counter1.get(curr, 0):
                left_char = s2[left]
                counter2[left_char] -= 1
                if counter2[left_char] == 0:
                    del counter2[left_char]
                left += 1
            
            if counter1 == counter2:
                return True
        

        return False








