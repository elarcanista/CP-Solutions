//Author: Andres-Felipe Ortega-Montoya
//CHEFSUM.cpp
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
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc){
    int n;
    cin >> n;
    int mi = 1<<30;
    int ind = -1;
    for(int i = 0; i < n; ++i){
      int temp;
      cin >> temp;
      if(temp < mi){
        mi = temp;
        ind = i+1;
      }
    }
    cout << ind << "\n";
  }
}
