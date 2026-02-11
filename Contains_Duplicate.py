from typing import List
class Solution:
    def hasDuplicate(self,nums : List[int]) -> bool:
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                return True
        return False
def main():
    nums = list(map(int,input("Enter numbers separated by space: ").split()))
    solution = Solution()
    result = solution.hasDuplicate(nums)
    print(result)
if __name__ == "__main__":
    main()
