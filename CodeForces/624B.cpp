#include <bits/stdc++.h>

using namespace std;
 
int main() {
	int n;
	cin >> n;
	priority_queue<long long> queue;
	for(int i = 0; i < n; i++){
		long long temp;
		cin >> temp;
		queue.push(temp);
	}
	long long last = queue.top();
	queue.pop();
	long long sum = last;
	int equ = 0;
	while(!queue.empty() && last > 0){
		long long temp = queue.top();
		queue.pop();
		if(temp - equ == last || temp >= last){
			++equ;
			temp = --last;
		}else{
			equ = 0;
		}
		last = temp;
		sum += temp;
	}
	cout << sum;
}
