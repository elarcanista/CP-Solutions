#include <bits/stdc++.h>
using namespace std;

class Graph{
public:
  //(index, degree)
  unordered_map<int,int> V;
  //(weight, (origin, destiny))
  set<tuple<int,int,int> > E;
  //(origin, (destiny, weight))
  unordered_map<int, unordered_map<int, int> > G;

  //O(1)
  bool addVertex(int index){
    if(V.count(index))
      return false;
    V[index] = 0;
    return true;
  }

  //O(log(n))
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
    for(auto &v:V){
      g.addVertex(v.first);
    }
    for(auto &e:E){
      cerr << get<2>(e) << " " << get<1>(e) << "r\n";
      g.addEdge(get<2>(e),get<1>(e),get<0>(e));
    }
    return g;
  }
};
