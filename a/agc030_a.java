import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = Integer.parseInt(sc.next());
        int b = Integer.parseInt(sc.next());
        int c = Integer.parseInt(sc.next());
        int ans = a + b + 1 >= c ? b + c : b + (a + b + 1);
        System.out.println(ans);
        sc.close();
    }
}