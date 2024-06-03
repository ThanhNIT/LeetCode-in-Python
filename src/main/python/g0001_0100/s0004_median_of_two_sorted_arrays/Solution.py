# #Hard #Top_100_Liked_Questions #Top_Interview_Questions #Array #Binary_Search #Divide_and_Conquer
# #Big_O_Time_O(log(min(N,M)))_Space_O(1) #2024_06_03_Time_63_ms_(99.35%)_Space_16.9_MB_(31.27%)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0
