import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = Integer.parseInt(sc.next());
        sc.next();
        for (int i = 0; i < h; i++) {
            String line = sc.next();
            System.out.println(line);
            System.out.println(line);
        }
        sc.close();
    }

}