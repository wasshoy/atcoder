import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        long[] a = new long[n];
        long x = 0;
        long y = 0;
        for (int i = 0; i < n; i++) {
            int ai = Integer.parseInt(sc.next());
            a[i] = ai;
            x += ai;
        }
        long ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            x -= a[i];
            y += a[i];
            ans = Math.min(ans, Math.abs(x - y));
        }
        System.out.println(ans);
        sc.close();
    }
}