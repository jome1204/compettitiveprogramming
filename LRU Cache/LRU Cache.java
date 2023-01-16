class LRUCache {

    private Map<Integer, Node> cache;
    private int capacity;

    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();

        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!cache.containsKey(key)) 
            return -1;
        remove(cache.get(key));
        insert(cache.get(key));
        return cache.get(key).val;
    }

    public void put(int key, int value) {
        if(cache.containsKey(key))
            remove(cache.get(key));
        cache.put(key, new Node(key, value));//if the node exsits update the value else create the new data
        insert(cache.get(key));
        
        if(cache.size() > capacity){
            Node lru = head.next;
            remove(lru);
            cache.remove(lru.key);
        }
    }

    public void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        node.next = node.prev = null;
    }
    public void insert(Node node) {
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
    }

    private class Node {

        private int key;
        private int val;

        Node next;
        Node prev;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
}
