//Author: Andres-Felipe Ortega-Montoya
//11228.cpp
#include <bits/stdc++.h>
//#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;
const int MAXV = 1000;
int state;
double road, rail;
ii vertices[MAXV];
vector< tuple<double, int, int> > edges;
int un[MAXV];
int rnk[MAXV];

void setUn(){
  for(int i = 0; i < MAXV; ++i)
    un[i] = i;
}

int find(int a){
  return un[a] == a? a : un[a] = find(un[a]);
}

bool merge(int a, int b){
  int x = find(a);
  int y = find(b);
  if(x != y){
    if (rnk[x] > rnk[y]) un[y] = x;
    else {
      un[x] = y;
      if (rnk[x] == rnk[y]) rnk[y]++;
    }
    return true;
  }
  return false;
}

int MST(int t){
  setUn();
  sort(edges.begin(), edges.end());
  int cost = 0;
  for(int i = 0; i < (int)edges.size(); ++i){
    bool f = merge(get<1>(edges[i]), get<2>(edges[i]));
    //get<1>(edges[i]) = round(get<1>(edges[i]));
    cost += (get<0>(edges[i])) * f;
    Debug(get<0>(edges[i]) << "\n");
    if(f){
      if(get<0>(edges[i]) > t){
        ++state;
        rail += get<0>(edges[i]);
      }else road += get<0>(edges[i]);
    }
  }
  return cost;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int TC;
  cin >> TC;
  for(int tc = 1; tc <= TC; ++tc){
    state = 1;
    road = rail = 0;
    edges.clear();
    memset(vertices,0,sizeof(vertices));
    int n, t;
    cin >> n >> t;
    for(int i = 0; i < n; ++i){
      int x, y;
      cin >> x >> y;
      vertices[i] = {x,y};
    }
    for(int i = 0; i < n; ++i){
      for(int j = i+1; j < n; ++j){
        int diffx = vertices[i].first - vertices[j].first;
        int diffy = vertices[i].second - vertices[j].second;
        double d = sqrt(diffx*diffx+diffy*diffy);
        edges.push_back({d,i,j});
      }
    }
    MST(t);
    cout << "Case #" << tc << ": " << state << " "
         << round(road) << " " << round(rail) << "\n";
  }
}
