//Author: Andres Felipe Ortega Montoya
//
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
typedef pair<int, int> ii;
 
const int INF = 1 << 30;
 
int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll n, a, b, c; cin >> n >> a >> b >> c;
  switch(n % 4){
  case 3:
    cout << min(a, min(b+c, 3*c));
    break;
  case 2:
    cout << min(a*2, min(b, c*2));
    break;
  case 1:
    cout << min(a*3, min(a+b, c));
    break;
  default:
    cout << 0;
  }
  cout << "\n";
}