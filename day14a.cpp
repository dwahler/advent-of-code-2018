#include "util.hpp"

using namespace std;

int main() {
    int target;
    cin >> target;

    list<int> board;
    board.push_back(3);
    board.push_back(7);
    list<int>::iterator it1 = board.begin();
    list<int>::iterator it2 = it1;
    it2++;

        cout << board << endl;
    int n = 2;
    vector<int> result;
    bool done = false;

    while (!done) {
        int a = *it1, b = *it2;
        int next = a+b;
        vector<int> buf;
        if (next == 0) {
            buf.push_back(0);
        }
        while (next > 0) {
            buf.push_back(next % 10);
            next /= 10;
        }
        reverse(buf.begin(), buf.end());
        for (auto i : buf) {
            //cout << "n=" << n << endl;
            if (n >= target + 10) {
                done = true;
                break;
            }
            if (n >= target) {
                result.push_back(i);
            }
            board.push_back(i);
            n++;

        }
        for (int i = 0; i < a+1; i++) {
            it1++;
            if (it1 == board.end()) it1 = board.begin();
        }
        for (int i = 0; i < b+1; i++) {
            it2++;
            if (it2 == board.end()) it2 = board.begin();
        }
        //cout << board << endl;
    }

    for (auto i : result) {
        cout << i;
    }
    cout << endl;
}
