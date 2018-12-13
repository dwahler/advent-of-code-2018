#include "util.hpp"
#include <algorithm>
#include <list>

using namespace std;

void fwd(list<int>& l, list<int>::iterator& it) {
    it++;
    if (it == l.end()) {
        it = l.begin();
    }
}
void back(list<int>& l, list<int>::iterator& it) {
    if (it == l.begin()) {
        it = l.end();
    }
    it--;
}


int main() {
    int players, marbles;
    cin >> players >> marbles;

    vector<long long> scores(players);
    list<int> circle;
    circle.push_back(0);
    list<int>::iterator ptr = circle.begin();
    
    for (int i = 1; i <= marbles; i++) {
        //cout << circle << circle[ptr] << endl;
        int pl = (i-1+players) % players;

        if (i % 23 != 0) {
            for (int j = 0; j < 2; j++) fwd(circle, ptr);
            ptr = circle.insert(ptr, i);
        } else {
            scores[pl] += i;
            for (int j = 0; j < 7; j++) back(circle, ptr);
            scores[pl] += *ptr;
            ptr = circle.erase(ptr);
            if (ptr == circle.end()) ptr = circle.begin();
        }
    }
    cout << *max_element(scores.begin(), scores.end()) << endl;
}
