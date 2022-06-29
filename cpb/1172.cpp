/*
Timelimit: 1
Read an array X[10]. After, replace every null or negative number of X ​by 1. Print all numbers stored in the array X.

Input
The input contains 10 integer numbers. These numbers ​​can be positive or negative.

Output
For each position of the array, print "X [i] = x", where i is the position of the array and x is the number stored in that position.


Input Sample	Output Sample
0
-5
63
0


X[0] = 1
X[1] = 1
X[2] = 63
X[3] = 1
...
*/
#include <iostream>>
using namespace std;

int main() {
    int X[10];
    for(int i = 0; i <= 9; i++) {
        cin >> X[i];
    }

    for(int i = 0; i <= 9; i++) {
        if(X[i] <= 0) {
            X[i] = 1;
        }
    }

    for(int i = 0; i <= 9; i++) {
        cout << "X[" << i << "] = " << X[i] << endl;
    }

    return 0;
}
