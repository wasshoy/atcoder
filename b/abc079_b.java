import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        var n = Integer.parseInt(sc.next());
        long[] lucas = new long[n + 1];
        lucas[0] = 2;
        lucas[1] = 1;
        for (int i = 2; i <= n; i++) {
            lucas[i] = lucas[i - 1] + lucas[i - 2];
        }
        System.out.println(lucas[n]);
        sc.close();
    }
}