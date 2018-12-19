#include "util.hpp"

using namespace std;

int main() {
    vector<string> board;
    for (string l : util::lines(cin)) {
        board.push_back(l);
    }

    const int N = board.size(), M = board[0].length();
    vector<string> next(board);
    for (long long iter = 0; iter < 100000L; iter++) {
        int tottree=0, totlumber=0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int tree=0, lumber=0;
                for (int i2 = max(i-1, 0); i2 <= min(i+1, N-1); i2++) {
                    for (int j2 = max(j-1, 0); j2 <= min(j+1, M-1); j2++) {
                        char c = board[i2][j2];
                        if (c == '|') tree++;
                        else if (c == '#') lumber++;
                    }
                }
                if (board[i][j] == '.') {
                    next[i][j] = tree >= 3 ? '|' : '.';
                } else if (board[i][j] == '|') {
                    next[i][j] = lumber >= 3 ? '#' : '|';
                } else {
                    next[i][j] = (lumber >= 2 && tree >= 1) ? '#' : '.';
                }
                if (next[i][j] == '|') tottree++;
                else if (next[i][j] == '#') totlumber++;
            }
        }
        if ((iter+1) % 28L == (1000000000L % 28L)) {
            cout << (iter+1) << " " << (tottree * totlumber) << endl;
        }
        swap(board,next);
    }
}
