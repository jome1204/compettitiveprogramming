class MedianFinder {
    private PriorityQueue<Integer> smaller;
    private PriorityQueue<Integer> bigger;
    private Integer median;

    public MedianFinder() {
        smaller=new PriorityQueue<>(new Comparator < Integer > () {
      @Override
      public int compare(Integer first, Integer second) {
        return (second - first);
      }
    });
        bigger=new PriorityQueue();
        median=null;

    }

    public void addNum(int num) {
         if (median != null) {
            if (num <= median) {
                smaller.offer(num);
                bigger.offer(median);
                median = null;
            } 
            else if (num >= median) {
                smaller.offer(median);
                bigger.offer(num);
                median = null;
            }            
        } else {
            if (smaller.peek() != null && num <= smaller.peek()) {
                smaller.offer(num);
                median = smaller.poll();
            }            
            else if (bigger.peek() != null && num >= bigger.peek()) {
                bigger.offer(num);
                median = bigger.poll();
            }
            else median = num;
        }

    }

    public double findMedian() {
      if (median != null) return median;
        else return smaller.peek() / 2.0 + bigger.peek() / 2.0;

    }
}
