import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int k = Integer.parseInt(sc.next());
        int count = n % 2 == 1 ? n / 2 + 1 : n / 2;

        String ans = count >= k ? "YES" : "NO";
        System.out.println(ans);
        sc.close();
    }
}