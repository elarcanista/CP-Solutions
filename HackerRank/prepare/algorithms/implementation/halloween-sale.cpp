// https://www.hackerrank.com/challenges/halloween-sale/
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
  int p, d, m, s, last, cont = 0;
  cin >> p >> d >> m >> s;
  last = p+d;
  while(s >= 0){
    ++cont;
    last = last-d > m? last-d : m;
    s -= last;
  }
  cout << --cont << "\n";
}
