#include <iostream>
using namespace std;

int main() {
	int n, t;
	string queue;
	cin >> n >> t >> queue;
	while(t--){
		for(int i = 0; i < n-1; ++i){
			if(queue[i] == 'B' && queue[i+1] == 'G'){
				queue[i] = 'G';
				queue[++i] = 'B';
			}
		}
	}
	cout << queue;
	return 0;
}
