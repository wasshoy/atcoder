import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long[] cookies = new long[4];
        long sum = 0;
        // 入力の受け取りと合計の計算
        for (int i = 0; i < 4; i++) {
            cookies[i] = sc.nextLong();
            sum += cookies[i];
        }
        sc.close();

        String ans = "No";
        // 2**4 通りの組み合わせを試す
        for (int i = 0; i < Math.pow(2, 4); i++) {
            long eaten = 0;
            for (int j = 0; j < 4; j++) {
                if ((1 & i >> j) == 1) {
                    eaten += cookies[j];
                }
            }
            if (sum == 2 * eaten) {
                ans = "Yes";
                break;
            }
        }
        System.out.println(ans);
    }
}