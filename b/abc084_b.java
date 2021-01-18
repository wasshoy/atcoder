import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = Integer.parseInt(sc.next());
        int b = Integer.parseInt(sc.next());
        String s = sc.next();
        boolean isOk = true;
        if (!s.contains("-"))
            isOk = false;
        String[] nums = s.split("-");
        if (nums.length != 2)
            isOk = false;
        else if (nums[0].length() != a || nums[1].length() != b)
            isOk = false;
        System.out.println(isOk ? "Yes" : "No");
        sc.close();
    }

}