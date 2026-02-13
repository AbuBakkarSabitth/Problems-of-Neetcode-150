from typing import List
class Solution:
    def groupAnagrams(self,strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagram_map:
                anagram_map[key]=[]
            anagram_map[key].append(word)

        return list(anagram_map.values())
def main():
    strd = input("Enter words separated by space: ").split()
    obj = Solution()
    print(obj.groupAnagrams(strd))
if __name__ == "__main__":
          main()
