class Solution {
    public boolean hasDuplicate(int[] nums) {

        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        Set<Integer> mySet = new HashSet<>();

        for (int n : nums ){
           boolean added =  mySet.add(n);

            if (!added) {
                return true;
            }
        }

        return false;
        
    }
}