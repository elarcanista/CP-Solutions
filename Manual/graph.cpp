#include <bits/stdc++.h>
#include "math.cpp"

using namespace std;

class HashInt3{
public:
  size_t operator() (tuple<int, int, int> const& key) const{
    vector<long long> t = {get<0>(key), get<1>(key), get<2>(key)};
    return cantorPairing(t);
  }
};

class Graph{
public:
  //(index, degree)
  unordered_map<int,int> V;
  //(weight, (origin, destiny))
  unordered_set<tuple<int,int,int>, HashInt3> E;
  //(origin, (destiny, weight))
  unordered_map<int, unordered_map<int, int> > G;

  //O(1)
  bool addVertex(int index){
    if(V.count(index))
      return false;
    V[index] = 0;
    return true;
  }

  //O(1)
  bool addEdge(int origin, int destiny, int weight){
    addVertex(origin);
    addVertex(destiny);
    if(E.count({weight,origin,destiny}))
      return false;
    V[destiny]++;
    E.insert({weight, origin, destiny});
    G[origin][destiny] = weight;
  }

  //O(|V|+|E|)
  Graph reverse(){
    Graph g;
    for(auto &v:V)
      g.addVertex(v.first);
    for(auto &e:E)
      g.addEdge(get<2>(e),get<1>(e),get<0>(e));
    return g;
  }
};
