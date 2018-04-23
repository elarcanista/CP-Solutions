#include <bits/stdc++.h>
using namespace std;

using uint = unsigned int;

//O(n^2), |M| = |W| = n
//Solution to the stable matching problem.
vector<int>deferredAcceptance(
  vector<vector<int> > men,
  vector<vector<int> > &women)
{
  vector<int> proposal;
  vector<bool> single;
  vector<vector<int> > preference;
  unsigned int nSingles = men.size();
  proposal.resize(women.size(), -1);
  single.resize(men.size(), true);
  preference.resize(women.size());
  //turns ranking order into preference by entry
  for(uint w = 0; w < women.size(); ++w){
    preference[w].resize(men.size(),-1);
    for(uint m = 0; m < men.size(); ++m){
      preference[w][women[w][m]] = m;
    }
  }
  while(nSingles){
    uint m;
    //first single men
    for(m = 0; m < men.size(); ++m)
      if(single[m])
        break;
    for(uint w = 0; w < men[m].size() && single[m]; ++w){
      //if woman w is not engaged, then propose
      if(proposal[w] == -1){
        proposal[w] = m;
        single[m] = false;
        --nSingles;
      }else if(preference[m] < preference[proposal[w]]){
        //if w prefers m to her current fiance, then propose
        single[proposal[w]] = true;
        proposal[w] = m;
        single[m] = false;
      }
    }
  }
  return proposal;
}
