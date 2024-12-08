class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        
        merged=[]
        
        intervals.append(newInterval)
        intervals.sort(key=lambda interval:interval[0])
        
        
        
        for interval in intervals:
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1][1]=max(merged[-1][1],interval[1])
        return merged        
        
