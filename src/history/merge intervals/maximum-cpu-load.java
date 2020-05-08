import java.util.*;

class Job {
  int start;
  int end;
  int cpuLoad;

  public Job(int start, int end, int cpuLoad) {
    this.start = start;
    this.end = end;
    this.cpuLoad = cpuLoad;
  }
};

class MaximumCPULoad {

  public static int findMaxCPULoad(List<Job> jobs) {
    Collections.sort(jobs, (a, b) -> a.start - b.start);

    PriorityQueue<Job> minHeap = new PriorityQueue<>(jobs.size(), (a, b) -> a.end - b.end);
    int result = 0;
    int temp = 0;
    for(Job job: jobs){
      while(!minHeap.isEmpty() && minHeap.peek().end <= job.start){
        temp -= minHeap.peek().cpuLoad;
        minHeap.poll();
      }
      
      minHeap.offer(job);
      temp += job.cpuLoad;
      result = Math.max(result, temp);
    }
    return result;
  }