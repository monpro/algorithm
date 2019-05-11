package Array;

public class findMedianSortedArrays_04 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int l = (m + n + 1) / 2;
        int r = (m + n + 2) / 2;
        return (getKthLargestElement(nums1, 0, nums2, 0, l) + getKthLargestElement(nums1, 0, nums2, 0, r)) / 2.0;
    }

    public double getKthLargestElement(int[] nums1, int aStart, int[] nums2, int bStart, int k){
        if(aStart > nums1.length - 1) return nums2[bStart + k - 1];
        if(bStart > nums2.length - 1) return nums1[aStart + k - 1];
        if( k == 1) return Math.min(nums1[aStart], nums2[bStart]);
        int aMid = Integer.MAX_VALUE, bMid = Integer.MAX_VALUE;
        if(aStart + k / 2 - 1 < nums1.length) aMid = nums1[aStart + k / 2 - 1];
        if(bStart + k / 2 - 1 < nums2.length) bMid = nums2[bStart + k / 2 - 1];
        if(aMid < bMid)
            return getKthLargestElement(nums1, aStart + k / 2, nums2, bStart, k - k / 2);
        else
            return getKthLargestElement(nums1, aStart, nums2, bStart + k / 2, k - k / 2);
    }
}
