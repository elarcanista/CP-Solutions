//Author: Andres-Felipe Ortega-Montoya
//11661.cpp
#include <bits/stdc++.h>
#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int s;
  while(cin >> s && s){
    string str;
    cin >> str;
    int lastr = -INF, lastd = -INF/2;
    int mindist = INF;
    for(int i = 0; i < s; ++i){
      if(str[i] == 'Z') mindist = 0;
      if(str[i] == 'D') lastd = i;
      if(str[i] == 'R') lastr = i;
      //      cout << lastr << " " << lastd << "\n";
      mindist = min(mindist, abs(lastr-lastd));
    }
    cout << mindist << "\n";
  }
}
