// https://www.hackerrank.com/challenges/angry-professor/
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC, count = 0, in;
  cin >> TC;
  while(TC--){
    int st, req;
    cin >> st >> req;
    while(st--){
      cin >> in;
      if(in <= 0) ++count;
    }
    cout << (count >= req? "NO": "YES") << "\n";
    count = 0;
  }
}
