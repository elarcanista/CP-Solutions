#include <bits/stdc++.h>
using namespace std;
//UVa 10067 - Playing with Wheels

unordered_set<int>forb;

int readInt(){ //reads a 4 digit number with digits separated by spaces
	int pot = 1000;
	int num = 0;
	int in;
	for(int i = 0 ; i < 4; ++i, pot /= 10){
		cin >> in;
		num += in * pot;
	}
	return num;
}

//bfs to check minimun distance
int bfs(int start, int target){
	if (start == target) return 0;
	queue<pair<int, int>>q;
	q.push({start, 0});
	forb.insert(start);
	while(!q.empty()){
		pair<int, int> t = q.front(); q.pop();
		int pot = 1000; 
		for(int i = 0; i < 4; ++i, pot /= 10){ // excecutes 1 time per digit
			int sum, res;
			int digit = (t.first / pot) % 10; //the digit to analyse
			if(digit == 9){  //changes the number
				sum = t.first - (digit * pot);
				res = t.first - pot;
			}else if(!digit){
				sum = t.first + pot;
				res = t.first + (9*pot);
			}else{
				sum = t.first + pot;
				res = t.first - pot;
			}
			if(sum == target || res == target)
				return t.second + 1;
			if(!forb.count(sum)){ // if is a new number, push it onto the queue and the forbiden set
				q.push({sum, t.second +1});
				forb.insert(sum);
			}
			if(!forb.count(res)){
				q.push({res, t.second +1});
				forb.insert(res);
			}
		}
	}
	return -1;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC, start, target; cin >>TC;
	while(TC--){
		forb.clear();
		start = readInt();
		target = readInt();
		int f;
		cin >> f;
		while(f--){
			int forbiden;
			forbiden = readInt();
			forb.insert(forbiden);
		}
		cout << bfs(start, target) << "\n";
	}
	return 0;
}
