#include "util.hpp"

#include <queue>
using namespace std;

int main() {
    vector<pair<int,int>> edges;

    for (string l : util::lines(cin)) {
        int a = l[5] - 'A';
        int b = l[36] - 'A';
        edges.push_back({a,b});
        cout << edges.back().first << "," << edges.back().second << endl;
    }

    {
        vector<int> counts(26);
        vector<bool> done(26);
        for (auto& a : edges) {
            counts[a.second]++;
        }
        cout << counts << endl;

        while (true) {
            int next = -1;
            for (int i = 0; i < 26; i++) {
                if (!done[i] && counts[i] == 0) {
                    next = i;
                    break;
                }
            }
            if (next == -1) break;

            done[next] = true;
            cout << (char) (next + 'A');
            for (auto& a : edges) {
                if (a.first == next) {
                    counts[a.second]--;
                }
            }
        }
        cout << endl;
    }

    {
        vector<int> counts(26);
        vector<bool> done(26);
        for (auto& a : edges) {
            counts[a.second]++;
        }
        cout << counts << endl;

        int t = 0;
        priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<pair<int,int>>> q;
        int active = 0;

        while (true) {
            bool added = false;
            cerr << "t=" << t << endl;
            if (q.size() < 5) {
                int next = -1;
                for (int i = 0; i < 26; i++) {
                    if (!done[i] && counts[i] == 0) {
                        next = i;
                        break;
                    }
                }
                cerr << "  start next=" << ((char) (next+'A')) << endl;
                if (next != -1) {
                    q.push({(t+next+61)*100+next, next});
                    done[next] = true;
                    added = true;
                }
            }
            if (!added) {
                if (q.size() > 0) {
                    pair<int, int> p = q.top();
                    q.pop();
                    t = p.first/100;
                    cerr << "  done " << ((char) (p.second+'A')) << endl;

                    for (auto& a : edges) {
                        if (a.first == p.second) {
                            counts[a.second]--;
                        }
                    }
                } else {
                    break;
                }
            }

        }
        cout << t << endl;
    }


}
