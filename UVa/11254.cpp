//Author: Andrés Felipe Ortega Montoya
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll s;
  while(cin >> s && s != -1){
    for(ll n = sqrt(2*s); n > 0; --n){
      ll a = (2*s - n*n + n)/(2*n);
      if(a*n + (n*n - n)/2 == s){
        cout << s << " = " << a << " + ... + " << a+n-1 << "\n";
        break;
      }
    }
  }
  return 0;
}
