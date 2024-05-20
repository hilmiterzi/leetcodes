class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_length = []
        saved_counted_letters = []
        for character in s:
            if character in saved_counted_letters:
                longest_length.append(len(saved_counted_letters))
                print("longest_length", longest_length)
                index = saved_counted_letters.index(character)
                print("index: ", index)
                saved_counted_letters = saved_counted_letters[index + 1:]
                print("saved_counted_letters: ", index+1)

            saved_counted_letters.append(character)
            print("saved_counted_letters: ", saved_counted_letters)

        longest_length.append(len(saved_counted_letters))
        print("longest_length: ", longest_length)
        return max(longest_length)
solution = Solution()
print(Solution.lengthOfLongestSubstring(solution, "abcddefgghikklmop"))