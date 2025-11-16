import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

public class AllInOne {
    // Пользовательский тип для PriorityQueue
    static final class Task {
        final long id;
        final String name;
        final int priority;

        Task(long id, String name, int priority) {
            this.id = id;
            this.name = name;
            this.priority = priority;
        }

        long id() { return id; }
        String name() { return name; }
        int priority() { return priority; }

        @Override
        public String toString() {
            return "Task{id=" + id + ", name=" + name + ", p=" + priority + "}";
        }
    }

    public static void main(String[] args) {
        nestedListsDemo();
        queueDemo();
        dequeDemo();
        primitivePriorityQueueDemo();
        customPriorityQueueDemo();
    }

    // --- Мультисписок (вложенный список) ---
    private static void nestedListsDemo() {
        System.out.println("=== Nested List ===");
        List<List<Integer>> multilist = new ArrayList<>();
        multilist.add(Arrays.asList(1, 2, 3));
        multilist.add(Arrays.asList(4, 5));
        multilist.add(Arrays.asList(6, 7, 8, 9));

        for (int i = 0; i < multilist.size(); i++) {
            List<Integer> row = multilist.get(i);
            int sum = row.stream().mapToInt(Integer::intValue).sum();
            System.out.println("row " + i + ": " + row + " | sum=" + sum);
        }
        System.out.println();
    }

    // --- Очередь (Queue + LinkedList) ---
    private static void queueDemo() {
        System.out.println("=== Queue< String > via LinkedList ===");
        Queue<String> queue = new LinkedList<>();
        queue.offer("A");
        queue.offer("B");
        queue.offer("C");

        System.out.println("size=" + queue.size());
        System.out.println("peek=" + queue.peek());
        while (!queue.isEmpty()) {
            System.out.println("poll=" + queue.poll());
        }
        System.out.println("empty=" + queue.isEmpty());
        System.out.println();
    }

    // --- Дек (ArrayDeque) ---
    private static void dequeDemo() {
        System.out.println("=== Deque< Integer > via ArrayDeque ===");
        Deque<Integer> deq = new ArrayDeque<>();
        deq.offerLast(1);   // хвост
        deq.offerFirst(2);  // голова
        deq.offerLast(3);

        System.out.println("front=" + deq.peekFirst() + " back=" + deq.peekLast());
        // изменим содержимое
        deq.pollFirst();   // убрать 2
        deq.offerFirst(5);
        deq.pollLast();    // убрать 3

        System.out.print("content: ");
        for (int x : deq) System.out.print(x + " ");
        System.out.println("\n");
    }

    // --- Приоритетная очередь (примитивы, natural order = min-heap по Integer) ---
    private static void primitivePriorityQueueDemo() {
        System.out.println("=== PriorityQueue<Integer> (min first) ===");
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(10);
        pq.offer(20);
        pq.offer(5);

        System.out.println("peek=" + pq.peek());
        while (!pq.isEmpty()) {
            System.out.print(pq.poll() + " ");
        }
        System.out.println("\n");
    }

    // --- Приоритетная очередь с компаратором (Task) ---
    private static void customPriorityQueueDemo() {
        System.out.println("=== PriorityQueue<Task> with Comparator ===");
        // Сортируем по приоритету возр. (меньшее число = выше приоритет),
        // при равенстве — по id возр. для стабильного детерминированного порядка
        Comparator<Task> byPriorityThenId =
                Comparator.comparingInt(Task::priority)
                          .thenComparingLong(Task::id);

        PriorityQueue<Task> pq = new PriorityQueue<>(byPriorityThenId);

        pq.add(new Task(10001, "Task 1", 5));
        pq.add(new Task(10003, "Task 3", 10));
        pq.add(new Task(10002, "Task 2", 1));
        pq.add(new Task(10005, "Task 5", 1)); // равный приоритет для проверки тай-брейкера

        System.out.println("peek=" + pq.peek());
        while (!pq.isEmpty()) {
            System.out.println(pq.poll());
        }
        System.out.println();
    }
}
