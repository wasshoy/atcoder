import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int ans = 0;
        if (n % 2 == 0)
            ans = n / 2 - 1;
        else
            ans = n / 2;
        System.out.println(ans);
        sc.close();
    }
}