import java.io.*;
import java.util.*;

class Main{
    public static void main(String [] args){
        Scanner in = new Scanner(System.in);
        int TC = in.nextInt();
        while(TC-- != 0){
            int a = in.nextInt();
            int b = in.nextInt();
            if(a>b)
                System.out.println(">");
            else if(a<b)
                System.out.println("<");
            else
                System.out.println("=");
        }
    }
}
