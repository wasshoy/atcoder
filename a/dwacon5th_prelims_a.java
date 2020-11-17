import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int sum = 0;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            int ai = Integer.parseInt(sc.next());
            sum += ai;
            a[i] = ai;
        }
        double avg = (double) sum / n;
        int ans = 0;
        double diff = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (Math.abs(a[i] - avg) < diff) {
                ans = i;
                diff = Math.abs(a[i] - avg);
            }
        }
        System.out.println(ans);
        sc.close();
    }
}