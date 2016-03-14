#include <bits/stdc++.h>
using namespace std;

int main(){
  //freopen("A-large-practice.in", "r", stdin);       reads input from file
	//freopen("A-large-practice.out", "w", stdout);     writes output to a file
    int TC; cin >> TC;
    for(int i = 1; i <= TC; ++i){
        int c, l; cin >> c >> l;
        map<int,vector<int> >s2;  //map with prize and all items who share that prize
        for(int j = 1; j <= l; ++j){
            int temp; cin >> temp;
            s2[temp].push_back(j);
        }
        int i1, i2;
        for(auto &a: s2){ //searchs if there is a item whose prize is the correct
            if(s2.count(c-a.first)){
                i1 = a.second[0];
                i2 = (i1 == s2[c-a.first][0])? s2[c-a.first][1]: s2[c-a.first][0];
                break;
            }
        }
        cout << "Case #" << i << ": " << min(i1,i2) << " " << max(i1,i2) << "\n";
    }
}
