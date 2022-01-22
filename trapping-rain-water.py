class Solution:
    def trap(self, height: List[int]) -> int:
        
        l_markers = []
        l_top = height[0]
        for i in range(len(height)):
            if height[i]>l_top:
                l_top = height[i]
                l_markers.append(l_top)
            else:
                l_markers.append(l_top)
  
        r_markers  = []
        r_top = height[-1]
        for i in range(len(height)-1, -1,-1):
            if height[i]>r_top:
                r_top = height[i]
                r_markers.append(r_top)
            else:
                r_markers.append(r_top)
                
        r_markers = r_markers[::-1]
        counter = 0
        for i in range(len(height)):
            counter+= min(l_markers[i], r_markers[i]) - height[i]
        return counter
