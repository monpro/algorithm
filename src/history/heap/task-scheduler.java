package history.heap;

import java.util.*;

class TaskScheduler {

  public static int scheduleTasks(char[] tasks, int k) {
    int intervalCount = 0;
    Map<Character, Integer> taskFrequencyMap = new HashMap<>();
    for (char chr : tasks)
      taskFrequencyMap.put(chr, taskFrequencyMap.getOrDefault(chr, 0) + 1);

    PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<Map.Entry<Character, Integer>>(
        (e1, e2) -> e2.getValue() - e1.getValue());

    // add all tasks to the max heap
    maxHeap.addAll(taskFrequencyMap.entrySet());

    while (!maxHeap.isEmpty()) {
      List<Map.Entry<Character, Integer>> waitList = new ArrayList<>();
      int n = k + 1; // try to execute as many as 'k+1' tasks from the max-heap
      for (; n > 0 && !maxHeap.isEmpty(); n--) {
        intervalCount++;
        Map.Entry<Character, Integer> currentEntry = maxHeap.poll();
        if (currentEntry.getValue() > 1) {
          currentEntry.setValue(currentEntry.getValue() - 1);
          waitList.add(currentEntry);
        }
      }
      maxHeap.addAll(waitList); // put all the waiting list back on the heap
      if (!maxHeap.isEmpty())
        intervalCount += n; // we'll be having 'n' idle intervals for the next iteration
    }

    return intervalCount;
  }

  public static void main(String[] args) {
    char[] tasks = new char[] { 'a', 'a', 'a', 'b', 'c', 'c' };
    System.out.println("Minimum intervals needed to execute all tasks: " + TaskScheduler.scheduleTasks(tasks, 2));

    tasks = new char[] { 'a', 'b', 'a' };
    System.out.println("Minimum intervals needed to execute all tasks: " + TaskScheduler.scheduleTasks(tasks, 3));
  }
}
