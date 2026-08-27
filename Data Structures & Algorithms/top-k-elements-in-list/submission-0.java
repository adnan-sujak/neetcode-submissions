class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> myMap = new HashMap<>();

        for(Integer number: nums) {
            myMap.put(number, myMap.getOrDefault(number, 0) + 1); //getOrDefault() Method returns the value of the entry in the map which has a specified key. If the entry does not exist
            // the value of the second parameter is returned
            // the numver itself is the key in the hashamp
        }

        List<Integer>[] buckets = new ArrayList[nums.length + 1];
        for (Map.Entry<Integer, Integer> entry : myMap.entrySet()) {
            int num = entry.getKey();
            int freq = entry.getValue();
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(num);
        }

        // Step 3: walk buckets from high freq to low and collect k elements
        int[] result = new int[k];
        int index = 0;

        for (int freq = buckets.length - 1; freq >= 0 && index < k; freq--) {
            if (buckets[freq] != null) {
                for (int num : buckets[freq]) {
                    result[index++] = num;
                    if (index == k) {
                        break;
                    }
                }
            }
        }

        return result;



    }
}
