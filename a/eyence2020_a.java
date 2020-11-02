import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = Integer.parseInt(sc.next());
        int w = Integer.parseInt(sc.next());
        int n = Integer.parseInt(sc.next());
        int max = Math.max(h, w);
        int ans = n % max == 0 ? n / max : n / max + 1;
        System.out.println(ans);
        sc.close();
    }
}