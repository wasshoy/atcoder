import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long a = Integer.parseInt(sc.next());
            long b = Integer.parseInt(sc.next());
            ans += (b * (b + 1)) / 2 - ((a - 1) * (a)) / 2;
        }
        System.out.println(ans);
        sc.close();
    }
}