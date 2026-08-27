class Solution {
     public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        // result[i] will store product of all elements to the LEFT of i
        result[0] = 1;
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // Now multiply by product of all elements to the RIGHT of i
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] = result[i] * rightProduct;
            rightProduct *= nums[i];
        }

        return result;
    }
}  
