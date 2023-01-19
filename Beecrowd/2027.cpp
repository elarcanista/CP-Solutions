//Author: Andrés Felipe Ortega Montoya
//URI 2027 - Noel Bet
#include <bits/stdc++.h>

using namespace std;

int GCDsimp (int num, int den) {
	//cout << num << den;
	if (den > 0){
		return GCDsimp (den, num % den);
	}
	return num;
}

int main() {
	int num, den, apostas [100], cont=-1;
	while (cin >> num >> den) {
		 apostas[++cont] = GCDsimp (num,den);
		 //cout << apostas[cont] << "\n";
		 if  ( apostas[cont] > 5)
			cout << "Noel\n" ;
		 else
			cout << "Gnomos" << endl;
	}
	for (int i= cont; i>= 0; --i) {
		cout << apostas[i] << " " ;
	}
	cout << "\n";
	return 0;
}
