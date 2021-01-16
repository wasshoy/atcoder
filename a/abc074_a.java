import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int a = Integer.parseInt(sc.next());
        int ans = n * n - a;
        System.out.println(ans);
        sc.close();
    }
}