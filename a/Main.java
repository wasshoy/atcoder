import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a, b;
        a = Integer.parseInt(sc.next());
        b = Integer.parseInt(sc.next());
        long ans = 2 * a + 100 - b;
        System.out.println(ans);
        sc.close();
    }
}