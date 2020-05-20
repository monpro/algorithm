class SearchBitonicArray {

    public static int search(int[] arr, int key) {
      int maxIndex = findMax(arr);
      int keyIndex = binarySearch(arr, key, 0, maxIndex);
      if (keyIndex != -1)
        return keyIndex;
      return binarySearch(arr, key, maxIndex + 1, arr.length - 1);
    }
  
    public static int findMax(int[] arr) {
      int start = 0, end = arr.length - 1;
      while (start < end) {
        int mid = start + (end - start) / 2;
        if (arr[mid] > arr[mid + 1]) {
          end = mid;
        } else {
          start = mid + 1;
        }
      }
  
      return start;
    }
  
    private static int binarySearch(int[] arr, int key, int start, int end) {
      while (start <= end) {
        int mid = start + (end - start) / 2;
  
        if (key == arr[mid])
          return mid;
  
        if (arr[start] < arr[end]) {
          if (key < arr[mid]) {
            end = mid - 1;
          } else { 
            start = mid + 1;
          }
        } else { 
          if (key > arr[mid]) {
            end = mid - 1;
          } else { 
            start = mid + 1;
          }
        }
      }
      return -1; 
    }
  
    public static void main(String[] args) {
      System.out.println(SearchBitonicArray.search(new int[] { 1, 3, 8, 9, 12, 4, 3 }, 4));
      System.out.println(SearchBitonicArray.search(new int[] { 3, 8, 3, 1 }, 8));
      System.out.println(SearchBitonicArray.search(new int[] { 1, 3, 8, 12 }, 12));
      System.out.println(SearchBitonicArray.search(new int[] { 10, 9, 8 }, 10));
    }
  }