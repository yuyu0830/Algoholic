#include <bits/stdc++.h>
#define int int64_t
using namespace std;

void sq(int i, int j, int N){
    if (i/N%3 == 1 && j/N%3 ==1){
        cout << ' ';
    } 
    else {
        if(N / 3 == 0)
            cout << "*";
        else 
            sq(i,j,N/3);
    }
    
}

int32_t main(){
    int N;
    cin >> N;
    
    for (int i=0; i<N; i++){
        for (int j=0; j<N; j++){
            sq(i,j,N);
        }
        cout << '\n';
    }

}

