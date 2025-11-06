import java.util.*;

public class Main {

    // Рекурсивная проверка по индексу i (слева направо)
    static boolean isSortedRecursive(int[] arr, int i) {
        if (arr == null || arr.length <= 1 || i >= arr.length - 1) {
            return true; // база: null, 0/1 элемент или дошли до конца [web:2][web:36]
        }
        if (arr[i] > arr[i + 1]) {
            return false; // нарушение порядка — неубывание не соблюдается [web:2][web:5]
        }
        return isSortedRecursive(arr, i + 1); // рекурсивно проверяем следующую пару [web:2][web:5]
    }

    // Удобная обёртка
    static boolean isSorted(int[] arr) {
        return isSortedRecursive(arr, 0); // старт с нулевого индекса [web:5]
    }

    public static void main(String[] args) {
        int[] a1 = {};                    // true [web:2][web:36]
        int[] a2 = {1};                   // true [web:2][web:36]
        int[] a3 = {1, 2, 2, 5};          // true [web:2][web:5]
        int[] a4 = {1, 3, 2};             // false [web:2][web:5]

        System.out.println(isSorted(a1));
        System.out.println(isSorted(a2));
        System.out.println(isSorted(a3));
        System.out.println(isSorted(a4));
    }
}
Результат работы:
true
true
true
false
