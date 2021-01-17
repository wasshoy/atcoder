
import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] w = sc.next().split("");
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String s : w) {
            if (!map.containsKey(s)) {
                map.put(s, 0);
            }
            map.replace(s, map.get(s), map.get(s) + 1);
        }
        boolean isOk = true;
        for (int v : map.values()) {
            if (v % 2 != 0) {
                isOk = false;
                break;
            }
        }
        System.out.println(isOk ? "Yes" : "No");
        sc.close();
    }
}