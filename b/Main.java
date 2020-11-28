import java.util.*;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = I(sc.next());
        int b = I(sc.next());
        int K = I(sc.next());
        for (int i = 0; i < K; i++) {
            if (i % 2 == 0) {
                if (a % 2 != 0)
                    a--;
                b += a / 2;
                a /= 2;
            } else {
                if (b % 2 != 0)
                    b--;
                a += b / 2;
                b /= 2;
            }
        }
        System.out.printf("%d %d\n", a, b);
        sc.close();
    }
}