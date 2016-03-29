//Author: Andrés Felipe Ortega Montoya
//UVa 12347 - Binary Search Tree
import java.util.*;
import java.lang.*;
import java.io.*;

class Ideone{
	public static void main (String[] args) throws java.lang.Exception{
		Scanner sc = new Scanner(System.in);
		int temp = sc.nextInt();
		tree t = new tree(temp);
		while(sc.hasNext()){
			temp = sc.nextInt();
			t.insert(temp);
		}
		t.print();
	}
}

class tree{
	int value;
	tree left;
	tree rigth;
	
	public tree(int num){
		value = num;
	}
	void print(){ //prints on postorder
		if(left != null) left.print();
		if(rigth != null) rigth.print();
		System.out.println(value);
	}
	void insert(int num){ //inserts a new node into tree
		if(num < value){ //if num < value insert left
			if(left == null){
				left = new tree(num);	
				return;
			}
			left.insert(num);
			return;
		}else if(rigth == null){ //if num > values insert rigth
			rigth = new tree(num);	
			return;
		}
		rigth.insert(num);
	}
}
