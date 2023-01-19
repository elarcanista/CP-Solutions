//Author: Andrés Felipe Ortega Montoya
//URI 1062 - Rails
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

vector<int> t;

bool sim(int n){
	stack<int> q;
	int i = 1;
	int index = 0;
	while(true){
		bool b = false;
		if(i == t[index]){
			b = true;
			//cout << i << " from A to B\n";
			++i;
			++index;
		}else if(!q.empty() && q.top() == t[index]){
			b = true;
			//cout << q.top() << " from Q to B\n";
			q.pop();
			++index;
		}else if(i <= n){
			//cout << i << " from A to Q\n";
			q.push(i);
			++i;
		}
		//cout << t[index] << " " << ((!q.empty())? q.top(): 0) << "\n";
		//cout << i << " " << b << "\n";
		//cout.flush();
		if(index >= t.size() || (i > n && !b) ) break;
	}
	return index >= t.size();
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	int c = 0;
	while(cin >> n && n){
		cin.ignore();
		string goal;
		//cout << (c++? "\n": "");
		while(getline(cin, goal) && goal != "0" && goal != ""){
			t.clear();
			stringstream ss(goal);
			int temp;
			while(ss >> temp){
				t.push_back(temp);
			}
			cout << (sim(n)? "Yes": "No") << "\n";
		}
		cout << "\n";
	}
	return 0;
}
