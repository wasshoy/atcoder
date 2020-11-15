import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long m = Integer.parseInt(sc.next());
        long d = Integer.parseInt(sc.next());
        int ans = 0;
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < d + 1; j++) {
                // System.out.printf("%d月%d日\n", i, j);
                int d_1 = j % 10;
                int d_10 = j / 10;
                // System.out.printf("%d, %d, %d\n", d_10, d_1, i);
                if ((d_1 >= 2) && (d_10 >= 2) && (d_1 * d_10 == i)) {
                    ans++;
                }

            }
        }
        System.out.println(ans);
        sc.close();
    }
}