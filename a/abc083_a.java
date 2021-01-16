import java.util.Scanner;

public class Main {
    public static int I(String s) {
        return Integer.parseInt(s);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int left = I(sc.next()) + I(sc.next());
        int right = I(sc.next()) + I(sc.next());
        System.out.println(left == right ? "Balanced" : left > right ? "Left" : "Right");
        sc.close();
    }
}