import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = Integer.parseInt(sc.next());
        int b = Integer.parseInt(sc.next());
        System.out.printf("%d %d\n", (a + b) / 2, (a - b) / 2);
    }
}