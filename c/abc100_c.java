import java.util.Scanner;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long ai = Integer.parseInt(sc.next());
            if (ai % 2 == 0) {
                while (ai % 2 == 0) {
                    ans += 1;
                    ai /= 2;
                }
            }
        }
        System.out.println(ans);
        sc.close();
    }
}