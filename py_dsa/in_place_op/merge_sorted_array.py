from typing import List
class ForwardMerge:
    '''
     nums1.length == m + n
     nums2.length == n
     0 <= m, n <= 200
     1 <= m + n <= 200
     -109 <= nums1[i], nums2[j] <= 109
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy1 = nums1[:m]
        i,j,k=0,0,0
        while i<m and j<n :
            if copy1[i] < nums2[j]:
                nums1[k] = copy1[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        
        if i<m:
            nums1[k:] = copy1[i:]
        
        if j<n:
            nums1[k:] = nums2[j:]



class BackwardMerge:
    '''
     nums1.length == m + n
     nums2.length == n
     0 <= m, n <= 200
     1 <= m + n <= 200
     -109 <= nums1[i], nums2[j] <= 109
    '''
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Follow up: Can you come up with an algorithm that runs in O(m + n) time?
        i,j,k = m-1,n-1,n+m-1
        while j>=0 :
            if i<0 or nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j-=1
            else:
                nums1[k] = nums1[i]
                i-=1
            k-=1