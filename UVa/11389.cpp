//Author: Andres Felipe Ortega Montoya
//UVa 11389 - The Bus Driver Problem
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int a,b,c, temp, cost, over;
  while(cin >> a >> b >> c && (a || b || c)){
    cost = 0;
    vector<int> m, e;
    for(int i = 0; i < a; ++i){
      cin >> temp;
      m.push_back(temp);
    }
    for(int i = 0; i < a; ++i){
      cin >> temp;
      e.push_back(temp);
    }
    sort(m.begin(), m.end());
    sort(e.begin(), e.end());
    for(int i = 0; i < a; ++i){
      over = m[i] + e[a-i-1] > b? m[i] + e[a-i-1] - b: 0;
      cost += over*c;
    }
    cout << cost << "\n";
  }
}
