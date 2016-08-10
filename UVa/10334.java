//Author: Andres Felipe Ortega Montoya
//UVa 10334 - Ray Through Glasses

import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

class Main{
	static HashMap<BigInteger, BigInteger> recall = new HashMap<>(); //stores values of fib
	static BigInteger zero = new BigInteger("0");
	static BigInteger one = new BigInteger("1");
		
	static BigInteger fib(BigInteger n){ //calculates fibonnacci, uses memoization
		if(recall.containsKey(n)) return recall.get(n);
		BigInteger ans = fib(n.subtract(one)).add(fib(n.subtract(one).subtract(one)));
		recall.put(n, ans);
		return ans;
	}
	public static void main (String[] args) throws java.lang.Exception{
		Scanner sc = new Scanner(System.in);
		int n;
		recall.put(zero, one);
		recall.put(one, one);
		while(sc.hasNext()){
			n = sc.nextInt();
			BigInteger ask = new BigInteger(Integer.toString(n));
			System.out.println(fib(ask.add(one)));
		}
	}
}
