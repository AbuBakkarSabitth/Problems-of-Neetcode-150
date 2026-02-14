from typing import List
import heapq
class Solution:
    def topKFrequent(self,nums: List[int],k:int)->List[int]:
        freq = {}
        min_heap = []
        for num in nums:
            freq[num] = freq.get(num,0)+1



        for num,count in freq.items():
            heapq.heappush(min_heap,(count,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result
        
        
       
            
            
def main():
    nums = list(map(int,input("enteer numbers: ").split()))
    k = int(input("Enteer the count numbers: "))
    obj = Solution()
    print(obj.topKFrequent(nums,k))
if __name__ == "__main__":
    main()
    
        
