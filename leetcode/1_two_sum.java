
/**
 * 1. Two Sum
 * Easy
 * Array, Hash Table
 * 
 * Map operations
 * 1. .containsKey()
 * 2. .get(<k>)
 * 3. .put(<k>, <v>)
 */

import java.util.Map;
import java.util.HashMap;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    // Create hash map
    Map<Integer, Integer> prevMap = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int diff = target - nums[i];

      if (prevMap.containsKey(diff)) {
        return new int[] { prevMap.get(diff), i };
      }
      prevMap.put(nums[i], i);
    }
    return new int[0]; // Guranteed solution, no need for return
  }
}
