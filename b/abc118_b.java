import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());
        int[] likes = new int[m];
        for (int i = 0; i < n; i++) {
            int k = Integer.parseInt(sc.next());
            for (int j = 0; j < k; j++) {
                int a = Integer.parseInt(sc.next());
                likes[a - 1]++;
            }
        }

        int ans = 0;
        for (int like : likes) {
            if (like == n)
                ans++;
        }
        System.out.println(ans);
        sc.close();
    }
}