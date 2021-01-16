import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int odd = 0;
        for (int i = 0; i < n; i++) {
            int ai = Integer.parseInt(sc.next());
            if (ai % 2 != 0) {
                odd++;
            }
        }
        String ans = odd % 2 == 0 ? "YES" : "NO";
        System.out.println(ans);
        sc.close();
    }
}