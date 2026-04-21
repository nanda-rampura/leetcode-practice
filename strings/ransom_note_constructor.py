from collections import defaultdict

class RansomNoteConstructor:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #store the magazine in dictionary
        magazineMap = defaultdict(int)
        for letter in magazine:
            magazineMap[letter] += 1

        for ch in ransomNote:
            if magazineMap[ch] < 1:
                return False
            magazineMap[ch] -= 1
                     
        return True
            