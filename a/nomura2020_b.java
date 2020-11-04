import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] t = sc.next().split("");
        for (int i = 0; i < t.length; i++) {
            if (t[i].equals("?")) {
                if (i > 0 && t[i - 1].equals("P")) {
                    t[i] = "D";
                } else if (i < t.length - 1 && t[i + 1].equals("D")) {
                    t[i] = "P";
                } else if (i < t.length - 1 && t[i + 1].equals("?")) {
                    t[i] = "P";
                } else {
                    t[i] = "D";
                }
            }
        }
        System.out.println("".join("", t));
        sc.close();
    }
}