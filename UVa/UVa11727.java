import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int TC = in.nextInt();
        for(int i = 1; i <= TC; ++i){
            int a = in.nextInt();
            int b = in.nextInt();
            int c = in.nextInt();
            System.out.printf("Case %d: %d\n", i, a+b+c
                              -Math.max(a,Math.max(b,c))
                              -Math.min(a,Math.min(b,c)));
        }
    }
}
