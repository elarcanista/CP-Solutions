import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int L = in.nextInt();
        while(L != 0){
            String road = in.next();
            int lastR = -L;
            int lastD = -L;
            int ans = L;
            for(int i = 0; i < L; ++i){
                if(road.charAt(i) == 'Z'){
                    ans = 0;
                    break;
                }
                if(road.charAt(i) == 'R'){
                    ans = Math.min(ans, i-lastD);
                    lastR = i;
                }
                if(road.charAt(i) == 'D'){
                    ans = Math.min(ans, i-lastR);
                    lastD = i;
                }
            }
            System.out.println(ans);
            L = in.nextInt();
        }
    }
}
