package Array;

public class ContainerWithMostWater_11 {
    public int maxArea(int[] height) {
        if(height.length <= 1){
            return 0;
        }
        int result = Integer.MIN_VALUE;
        int left = 0, right = height.length - 1;
        while (left < right){
            result = Math.max(result, (right - left) * Math.min(height[left], height[right]));
            if(height[left] < height[right])
                left ++;
            else
                right --;
        }
        return result;
    }

    public static void main(String[] args){
        ContainerWithMostWater_11 solution = new ContainerWithMostWater_11();
        System.out.println(solution.maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
        System.out.println(solution.maxArea(new int[]{1,2}));
    }
}
