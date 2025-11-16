import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Москва");
        list.add("Воронеж");
        list.add("Новгород");

        // Печать списка целиком
        System.out.println("list = " + list);

        // Печать по одному элементу
        for (String city : list) {
            System.out.println(city);
        }

        // Размер списка
        System.out.println("size = " + list.size());
    }
}
