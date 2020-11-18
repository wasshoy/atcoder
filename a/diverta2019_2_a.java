import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int k = Integer.parseInt(sc.next());
        int ans = k != 1 ? n - k : 0;
        System.out.println(ans);
        sc.close();
    }
}