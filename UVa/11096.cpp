#Author: Andres Felipe Ortega Montoya
#UVa 11096 - Nails
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
double EPS = 1e-9;

struct poll{
  ll x, y;
  poll(){
    x = y = 0.0;
  }
  poll(ll _x, ll _y):
    x(_x),
    y(_y){}
  
  bool operator < (poll other) const{
    if(fabs(y-other.y) > EPS)
      return y < other.y;
    return x < other.x;
  }

  bool operator == (poll other) const{
    return (fabs(x-other.x) < EPS && (fabs(y - other.y < EPS)));
  }
};

ll TC;

struct vec {
  ll x, y;
  vec(ll _x, ll _y) : x(_x), y(_y) {}
};

vec toVec(poll a, poll b) {
  return vec(b.x -a.x, b.y - a.y);
}

ll cross(vec a, vec b) {
  return a.x * b.y - a.y*b.x;
}

bool ccw(poll p, poll q, poll r) {
  return cross(toVec(p, q), toVec(p, r)) >= 0;
}

bool collinear(poll p, poll q, poll r) {
  return fabs(cross(toVec(p, q), toVec(p, r))) < EPS;
}

double dist(poll p1, poll p2){
  return hypot(p1.x-p2.x, p1.y-p2.y);
}
  
vector<poll> P;
double distancia;
ll r;

poll pivot(0,0);

bool angleCmp(poll a, poll b){
  if(collinear(pivot, a, b))
    return dist(pivot, a) < dist(pivot, b);
  ll d1x = a.x - pivot.x, d1y = a.y - pivot.y;
  ll d2x = b.x - pivot.x, d2y = b.y - pivot.y;
  return (atan2(d1y, d1x) - atan2(d2y, d2x)) < 0;
}

vector<poll> CH(){
  ll i, j, n = (ll)P.size();
  if(n <= 3){
    if(!(P[0] == P[n-1]))
      P.push_back(P[0]);
    return P;
  }

  ll P0 = 0;
  for(i = 1; i < n; ++i){
    if(P[i].x < P[P0].x || (P[i].x == P[P0].x && P[i].y < P[P0].y)){
      P0 = i;
    }
  }

  poll temp = P[0];
  P[0] = P[P0];
  P[P0] = temp;

  pivot = P[0];
  sort(++P.begin(), P.end(), angleCmp);
  vector<poll> S;
  S.push_back(P[n-1]);
  S.push_back(P[0]);
  S.push_back(P[1]);
  i = 2;
  while(i < n){
    j = (ll)S.size()-1;
    if(ccw(S[j-1], S[j], P[i]))
      S.push_back(P[i++]);
    else
      S.pop_back();
  }
  return S;
}

int main() {
  //ios_base::sync_with_stdio(false);
  //cin.tie(NULL);
  cout << setprecision(7) << fixed;
  cin >> TC;
  ll t;
  while(TC--){
    P.clear();
    distancia = 0;
    cin >> r >> t;
    //cout << r << " " << t << " ";
    for(ll i = 0; i < t; ++i){
      ll x, y;
      cin >> x >> y;
      P.push_back(poll(x,y));
    }
    if(t == 2){
      distancia = dist(P[0], P[1])*2;
      //  cout << "2 ";
    }else if(t == 1){
      //cout << "1 ";
      distancia = 0;
    }else{
      //cout << "3 ";
      sort(P.begin(), P.end());
      pivot = P[0];
      vector<poll> S = CH();
      for(ll i = 0; i < (ll)S.size()-1; ++i){
	distancia += dist(S[i], S[i+1]);
      }
    }
    distancia = max((double)r, distancia);
    printf("%.5lf\n", distancia);
    /*if(r > distancia){
      cout << r << "\n";
    }else{
      cout << distancia << "\n";
    }*/
  }
  return 0;
}
