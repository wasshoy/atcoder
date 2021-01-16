
// 22m AC
import java.util.Scanner;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = I(sc.next());
        int a = I(sc.next());
        int b = I(sc.next());
        int now = 0;
        for (int i = 0; i < n; i++) {
            String s = sc.next();
            int d = I(sc.next());
            now += (s.equals("East") ? 1 : -1) * (d < a ? a : d > b ? b : d);
        }
        String ans = now == 0 ? "0" : now > 0 ? String.format("East %d", now) : String.format("West %d", -now);
        System.out.println(ans);
        sc.close();
    }
}