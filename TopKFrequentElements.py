from typing import List
class Solution:
    def topKFrequent(self,nums:List[int],k:int) -> List[int]:
        repeat = []
        freq = {}

        for j in nums:
            count =0
            for i in range(len(nums)):
                if nums[i] == j:
                    count+=1
            freq[j] = count
        sorted_items= sorted(freq.items(),key = lambda x:x[1], reverse = True)
        for i in range(k):
            repeat.append(sorted_items[i][0])
        return repeat
def main():
    nums = list(map(int,input("enteer numbers: ").split()))
    k = int(input("Enteer the count numbers: "))
    obj = Solution()
    print(obj.topKFrequent(nums,k))
if __name__ == "__main__":
    main()
    
        
