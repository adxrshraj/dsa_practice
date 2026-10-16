class Solution:
    def segregate0and1(self, arr):
        # code here
        a = 0
        b = 0
        
        for i in arr:
            if i == 0:
                temp = arr[b]
                arr[b] = arr[a]
                arr[a] = temp
                b += 1
            a += 1
                
        return arr
            
