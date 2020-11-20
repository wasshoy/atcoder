import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        String s = sc.next();
        int redCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'R')
                redCount++;
        }
        String ans = redCount > n - redCount ? "Yes" : "No";
        System.out.println(ans);
        sc.close();
    }
}