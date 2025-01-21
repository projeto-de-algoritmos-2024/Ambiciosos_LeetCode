class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
            
        satisfaction.sort(reverse=True)

        total_sum = 0  
        current_sum = 0 
        max_sum = 0 

        for sat in satisfaction:
            current_sum += sat
            total_sum += current_sum
            max_sum = max(max_sum, total_sum)
            
            if current_sum <= 0:
                break

        return max_sum
