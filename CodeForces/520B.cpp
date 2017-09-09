#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m; cin >> n >> m;
	set<int> s; //avoid repeating operations
	queue<pair<int, int>> q; //bfs queue
	s.insert(n);
	q.push({n, 0});
	while(!q.empty()){
		pair<int, int> p = q.front(); q.pop();
		int mult = p.first*2;
		int sub = p.first - 1;
		if(mult == m || sub == m){ //if goal has been reached
			cout << p.second + 1 << '\n';
			break;
		}
		if(mult < 2*m && !s.count(mult)){ //beause 2m would only be obtained from having already m, all grater values aren't necesary
			q.push({mult, p.second + 1});
			s.insert(mult);
		}
		if(sub > 0 && !s.count(sub)){ //machine breaks on negatives
			q.push({sub, p.second + 1});
			s.insert(sub);
		}
	}
}
