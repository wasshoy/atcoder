import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] ns = new String[4];
        for (int i = 0; i < 4; i++) {
            ns[i] = sc.next();
        }
        ;
        String ans = "NO";
        if (Arrays.asList(ns).contains("1") && Arrays.asList(ns).contains("7") && Arrays.asList(ns).contains("9")
                && Arrays.asList(ns).contains("4")) {
            ans = "YES";
        }
        System.out.println(ans);
        sc.close();
    }
}