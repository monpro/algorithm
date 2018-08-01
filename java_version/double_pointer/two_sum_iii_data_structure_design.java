package double_pointer;

import java.util.HashMap;
import java.util.Map;

/*
Design and implement a TwoSum class.
It should support the following operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
 */
public class two_sum_iii_data_structure_design {

    Map<Integer, Integer> map = new HashMap<>();
    public void add(int number) {
        // write your code here
        map.put(number, map.getOrDefault(number,0) + 1);
    }

    /**
     * @param value: An integer
     * @return: Find if there exists any pair of numbers which sum is equal to the value.
     */
    public boolean find(int value) {
        // write your code here
        int result;
        for(int i: map.keySet()){
            result = value - i;
            if(map.containsKey(result)){
                if(result != i || map.get(i) > 1){
                    return true;
                }
            }
        }
        return false;
    }
}
