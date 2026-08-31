import java.util.*;

class TimeMap {

    private Map<String, TreeMap<Integer, String>> store;

    public TimeMap() {
        this.store = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if (store.containsKey(key)) {
            store.get(key).put(timestamp, value);
            return;
        }

        TreeMap<Integer, String> tree = new TreeMap<>();
        tree.put(timestamp, value);
        store.put(key, tree);
    }

    public String get(String key, int timestamp) {
        if (store.containsKey(key)){
           var entry = store.get(key).floorEntry(timestamp);
           if(entry != null) return entry.getValue();
        }
        return "";
    }
}
