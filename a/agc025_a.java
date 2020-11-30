import java.util.*;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = I(sc.next());
        int ans = Integer.MAX_VALUE;
        for (int i = 1; i < n / 2 + 1; i++) {
            int a = i;
            int b = n - a;
            int res = 0;
            while (a > 0 || b > 0) {
                res += a % 10 + b % 10;
                a /= 10;
                b /= 10;
            }
            ans = Math.min(ans, res);
        }
        System.out.println(ans);
        sc.close();
    }
}