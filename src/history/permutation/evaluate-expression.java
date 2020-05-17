package history.permutation;

import java.util.*;

class EvaluateExpression {
  static Map<String, List<Integer>> cache = new HashMap<>();
  public static List<Integer> diffWaysToEvaluateExpression(String input) {
    if(cache.containsKey(input)){
      return cache.get(input);
    }
    List<Integer> result = new ArrayList<>();
    if(!input.contains("+") && !input.contains("-") && !input.contains("*")){
      result.add(Integer.parseInt(input));
    }else{
      for(int i = 0; i < input.length(); i++){
        char ch = input.charAt(i);
        if(!Character.isDigit(ch)){
          List<Integer> left = diffWaysToEvaluateExpression(input.substring(0, i));
          List<Integer> right = diffWaysToEvaluateExpression(input.substring(i + 1));

          for(int num1: left){
            for(int num2: right){
              if(ch == '+'){
                result.add(num1 + num2);
              }
              else if(ch == '-'){
                result.add(num1 - num2);
              }else if(ch == '*'){
                result.add(num1 * num2);
              }
            }
          }
        }
      }
      cache.put(input, result);
    }
    return result;
  }
}