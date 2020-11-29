import java.util.*;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = I(sc.next());
        int b = I(sc.next());
        int d = b - a;
        int tb = d * (d + 1) / 2;
        int ta = tb - d;
        int ans = ta - a;
        System.out.println(ans);
        sc.close();
    }
}