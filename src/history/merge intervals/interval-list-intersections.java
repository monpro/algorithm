import java.util.*;

class Interval {
  int start;
  int end;

  public Interval(int start, int end) {
    this.start = start;
    this.end = end;
  }
};

class IntervalsIntersection {

  public static Interval[] merge(Interval[] arr1, Interval[] arr2) {
    List<Interval> intervalsIntersection = new ArrayList<Interval>();
    int i = 0, j = 0;

    while(i < arr1.length && j < arr2.length){
      if(arr1[i].start >= arr2[j].start && arr1[i].start <= arr2[j].end ||
        arr2[j].start >= arr1[i].start && arr2[j].start <= arr1[j].end){
          intervalsIntersection.add(new Interval(Math.max(arr1[i].start, arr2[j].start), 
                                                  Math.min(arr1[j].end, arr2[j].end)));
        }
      if(arr1[i].end < arr2[j].end){
        i += 1;
      }
      else{
        j += 1;
      }
    }


    return intervalsIntersection.toArray(new Interval[intervalsIntersection.size()]);
  }