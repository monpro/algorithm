class Solution {
    class Pair {
        int index;
        int val;
        public Pair(int index, int val) {
            this.index = index;
            this.val = val;
        }
    }

    public List<Integer> countSmaller(int[] nums) {
        List<Integer> result = new ArrayList<>();
        if(nums == null || nums.length == 0)
            return result;
        Pair[] mergeArray = new Pair[nums.length];
        Integer[] smaller = new Integer[nums.length];
        Arrays.fill(smaller, 0);
        for (int i = 0; i < nums.length; i++) {
            mergeArray[i] = new Pair(i, nums[i]);
        }
        mergeSort(mergeArray, smaller);
        result.addAll(Arrays.asList(smaller));
        return result;
    }
    
    private Pair[] mergeSort(Pair[] arr, Integer[] smaller){
        if(arr.length <= 1)
            return arr;
        int mid = arr.length / 2;
        
        Pair[] left = mergeSort(Arrays.copyOfRange(arr, 0, mid), smaller);
        Pair[] right = mergeSort(Arrays.copyOfRange(arr, mid, arr.length), smaller);
        
        int i = 0, j = 0;
        while(i < left.length || j < right.length){
            if(j == right.length || i < left.length && left[i].val <= right[j].val){
                arr[i + j] = left[i];
                smaller[left[i].index] += j;
                i += 1;
            }else{
                arr[i + j] = right[j];
                j += 1;
            }
        }
        return arr;
    }
    
}