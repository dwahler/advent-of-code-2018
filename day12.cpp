#include "util.hpp"

using namespace std;

int main() {
    //for (string l : util::lines(cin)) {
    //}
    string word, initial;
    cin >> word >> word >> initial;

    vector<bool> table(32);
    for (int i = 0; i < 32; i++) {
        string a, b;
        cin >> a >> word >> b;
        int mask = 0;
        for (int i = 0; i < 5; i++) {
            if (a[i] == '#') {
                mask |= (1<<i);
            }
        }
        table[mask] = (b == "#");
    }
    for (int i = 0; i < 32; i++) {
        cout << table[i] << endl;
    }

    vector<bool> state(100000);
    for (int i = 0; i < initial.length(); i++) {
        state[50000+i] = initial[i] == '#';
    }


    int last = 0;
    for (int i = 0; i < 50000; i++) {
        int a=99999, b=-9999;

        vector<bool> next(100000);
        for (int j = 0+2; j < 100000-2; j++) {
            int mask = 0;
            for (int k = 0; k < 5; k++) {
                if (state[j-2+k]) mask |= (1<<k);
            }
            next[j] = table[mask];
            if (table[mask]) {
                a = min(j,a);
                b = max(j,b);
            }
        }

        /*a = 490;
        for (int j = a; j <= b; j++) {
            cout << (next[j]?"#":":");
        }
        cout << a;
        cout << endl;
        */
        state = next;
        int total = 0;
        for (int i = 0; i < 100000; i++) {
            if (state[i]) total += i-50000;
        }
        cout << i << " " << total << " " << (total-last) << endl;
        last = total;
    }


}
