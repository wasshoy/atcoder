import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String t = sc.next();
        if (s.equals("Y")) {
            t = t.toUpperCase();
        }
        System.out.println(t);
        sc.close();
    }
}