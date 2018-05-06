//Author: Andres-Felipe Ortega-Montoya
//kruskal.cpp
#include <bits/stdc++.h>
#include "disjointSet.cpp"

using namespace std;

//O(
//
int MST(vector< tuple<int, int, int> > &edges, int t){
  disjointSets cc(edges.size());
  sort(edges.begin(), edges.end());
  int cost = 0;
  for(unsigned int i = 0; i < (int)edges.size(); ++i){
    bool f = merge(get<1>(edges[i]), get<2>(edges[i]));
    cost += (get<0>(edges[i])) * f;
  }
  return cost;
}
