//Author: Andres-Felipe Ortega-Montoya
//SEACO.cpp
#include <bits/stdc++.h>
#define DEBUG
#ifdef DEBUG
#define Debug(x) cout << x
#else
#define Debug(x)
#endif
#define op(x,op,y) ((((x)%MOD) op ((y)%MOD)) % MOD)

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;

const ll INF = 1 << 30;
const ll MAXN = 1000000;
const ll MOD = 1000000007;

ll treeq [4*MAXN];
ll treea [4*MAXN];
ll lazyq [4*MAXN];
ll lazya [4*MAXN];
tuple<ll,ll,ll> queries [4*MAXN];

void prop(ll* tree, ll* lazy, ll node,ll l,ll r){
  ll la = *(lazy + node)%MOD;
  *(tree + node) = op(*(tree + node),+, op(la,*,(r-l+1)));
  if(l!=r){
    *(lazy + node*2) = op(*(lazy + node*2),+, la);
    *(lazy + node*2+1) = op(*(lazy + node*2+1),+, la);
  }
  *(lazy + node) = 0;
}

void update(ll* tree, ll* lazy, ll node, ll l, ll r, ll a, ll b, ll p){
  ll mid = (l+r)/2;
  if(l > r || l > b || r < a) return;
  prop(tree, lazy, node, l, r);
  if(l >= a && r <= b){
    *(tree + node) = op(*(tree + node),+, op(p,*,(r-l+1)));
    if(l != r){
      *(lazy + node*2) = op(*(lazy + node*2),+, p);
      *(lazy + node*2+1) = op(*(lazy + node*2+1),+, p);
    }
    return;
  }
  update(tree, lazy, node*2, l, mid, a, b, p);
  update(tree, lazy, node*2+1, mid+1, r, a, b, p);
  *(tree + node) = op(*(tree + node*2),+, *(tree + node*2+1));
}

ll query(ll* tree, ll* lazy, ll node, ll l, ll r, ll a){
  ll mid = (l+r)/2;
  if(l > r || l > a || r < a) return 0;
  prop(tree, lazy, node, l, r);
  if(l == r){
    return *(tree+node);
  }
  ll t1 = query(tree, lazy, node*2, l, mid, a);
  ll t2 = query(tree, lazy, node*2+1, mid+1, r, a);
  return op(t1,+, t2);
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll TC;
  cin >> TC;
  for(ll tc = 1; tc <= TC; ++tc){
    memset(treeq, 0, sizeof(treeq));
    memset(treea, 0, sizeof(treea));
    memset(lazyq, 0, sizeof(lazyq));
    memset(lazya, 0, sizeof(lazya));
    memset(queries, 0, sizeof(queries));
    ll n, q;
    cin >> n >> q;
    ll n2 = 1 << (ll)ceil(log2(n));
    ll q2 = 1 << (ll)ceil(log2(q));
    for(ll i = 1; i <= q; ++i){
      ll a,b,c;
      cin >> a >> b >> c;
      queries[i] = {a,b,c};
    }
    update(treeq, lazyq, 1, 1, q2, 1, q, 1);
    //    pq(q, q2);
    for(ll i = q; i > 0; --i){
      tuple<ll, ll, ll> t = queries[i];
      if(get<0>(t) == 2){
        ll p = query(treeq, lazyq, 1, 1, q2, i) % MOD;
        update(treeq, lazyq, 1, 1, q2, get<1>(t), get<2>(t), p);
      }
    }
    for(ll i = q; i > 0; --i){
      tuple<ll, ll, ll> t = queries[i];
      if(get<0>(t) == 1){
        ll p = query(treeq, lazyq, 1, 1, q2, i) % MOD;
        update(treea, lazya, 1, 1, n2, get<1>(t), get<2>(t), p);
      }
    }
    cout << query(treea,lazya,1,1,n2,1) % MOD;
    for(ll i = 2; i <= n; ++i){
      cout << " " << query(treea,lazya,1,1,n2,i) % MOD;;
    }
    cout << "\n";
    /*cout << query(treeq,lazyq,1,1,q2,1) % MOD;
    for(ll i = 2; i <= q; ++i){
      cout << " " << query(treeq,lazyq,1,1,q2,i) % MOD;
      }
    cout << "\n";
    for(ll i = 1; i <= q2; ++i){
      cout << " " << lazyq[i] << lazya[i];
    }
    cout << "\n";*/
  }
}
