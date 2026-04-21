class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict()
        max_length = 0
        start = 0
        for end, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            
            seen[ch] = end
            max_length = max(max_length, end - start + 1)

        return max_length

