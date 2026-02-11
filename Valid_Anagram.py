class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)):
            return False
        if sorted(s) == sorted(t):
            return True
        return False
def main():
    s = input("Enter first string: ")
    t = input("Enter second string: ")
    solution = Solution()
    result = solution.isAnagram(s,t)
    print(result)
if __name__ == "__main__":
    main()
