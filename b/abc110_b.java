import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int m = Integer.parseInt(sc.next());
        int X = Integer.parseInt(sc.next());
        int Y = Integer.parseInt(sc.next());
        int[] x = new int[n];
        int[] y = new int[m];
        for (int i = 0; i < n; i++) {
            x[i] = Integer.parseInt(sc.next());
        }
        for (int i = 0; i < m; i++) {
            y[i] = Integer.parseInt(sc.next());
        }
        int[] cands = new int[Y - X];
        for (int i = 0; i < Y - X; i++)
            cands[i] = X + i + 1;
        Arrays.sort(x);
        Arrays.sort(y);
        int max_x = x[n - 1];
        int min_y = y[0];
        int cnt = 0;
        for (int z : cands) {
            cnt += (max_x < z && z <= min_y) ? 1 : 0;
        }
        if (cnt == 0) {
            System.out.println("War");
        } else {
            System.out.println("No War");
        }
        sc.close();
    }
}