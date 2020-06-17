package heap;

import java.util.*;
class FrequencyNumber {
  int order;
  int frequency;
  int value;

  public FrequencyNumber(int order, int frequency, int value){
    this.order = order;
    this.frequency = frequency;
    this.value = value;
  }
}


class FrequencyNumberComparator implements Comparator<FrequencyNumber>{
  public int compare(FrequencyNumber e1, FrequencyNumber e2){
    if(e1.frequency == e2.frequency){
      return e2.order - e1.order;
    }
    return e2.frequency - e1.frequency;
  }
}

class FrequencyStack {
  int order = 0;
  PriorityQueue<FrequencyNumber> maxHeap = new PriorityQueue<>(new FrequencyNumberComparator());
  Map<Integer, Integer> count = new HashMap<>();

  public void push(int num) {
    order += 1;
    count.put(num, count.getOrDefault(num, 0) + 1);
    maxHeap.add(new FrequencyNumber(order, count.get(num), num));
  }

  public int pop() {
    FrequencyNumber frequencyNum = maxHeap.poll();

    if(frequencyNum.frequency > 1){
      count.put(frequencyNum.value,  count.get(frequencyNum.frequency) - 1);
    }else{
      count.remove(frequencyNum);
    }
    // TODO: Write your code here
    return frequencyNum.value;
  }

  public static void main(String[] args) {
    FrequencyStack frequencyStack = new FrequencyStack();
    frequencyStack.push(1);
    frequencyStack.push(2);
    frequencyStack.push(3);
    frequencyStack.push(2);
    frequencyStack.push(1);
    frequencyStack.push(2);
    frequencyStack.push(5);
    System.out.println(frequencyStack.pop());
    System.out.println(frequencyStack.pop());
    System.out.println(frequencyStack.pop());
  }
}
