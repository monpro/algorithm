package arrays;

class Solution {
    int count = 0;
    int lower = 0;
    int upper = 0;
    
    public int countRangeSum(int[] nums, int lower, int upper) {
        this.lower = lower;
        this.upper = upper;
        
        long[] sums = new long[nums.length + 1];
        sums[0] = 0;
        long[] temp = new long[nums.length + 1];
        for(int i = 1; i <= nums.length; i++){
            sums[i] = sums[i - 1] + (long)nums[i - 1];
        }
        
        mergeSort(sums, 0, sums.length - 1, temp);
        return count;
    }
    
    public void mergeSort(long[] arr, int start, int end, long[] temp){
        if(start < end){
            int mid = start + (end - start) / 2;
            mergeSort(arr, start, mid, temp);
            mergeSort(arr, mid + 1, end, temp);
            merge(arr, start, mid, end, temp);
        }
    }
    
    public void merge(long[] arr, int start, int mid, int end, long[] temp){
        int startIndex = mid + 1, endIndex = mid + 1;
        for(int i = start; i <= mid; i++){
            while(startIndex <= end && arr[startIndex] - arr[i] < lower){
                startIndex += 1;
            }
            while(endIndex <= end && arr[endIndex] - arr[i] <= upper){
                endIndex += 1;
            }
            
            count += endIndex - startIndex;
        }
        
        int index = start;
        int left = start, right = mid + 1;
        while(left <= mid && right <= end){
            if(arr[left] < arr[right]){
                temp[index++] = arr[left++];
            }else{
                temp[index++] = arr[right++];
            }
        }
        
        while(left <= mid){
            temp[index++] = arr[left++];
        }
        
        while(right <= end){
            temp[index++] = arr[right++];
        }
        
        for(int i = start; i <= end; i++){
            arr[i] = temp[i];
        }
    }
    
}