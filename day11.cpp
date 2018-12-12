#include "util.hpp"

using namespace std;

int main() {
    const int serial = 9005;

    vector<vector<int>> cells(400, vector<int>(300));

    for (int x = 0; x < 300; x++) {
        for (int y = 0; y < 300; y++) {
            int power = (x+10)*y;
            power += serial;
            power *= (x+10);
            power = (power / 100) % 10;
            power -= 5;
            cells[x][y] = power;
            //cout << cells[x][y] << endl;
        }
    }

    int m = -9999;
    int mx = -1, my = -1, ms = -1;
    for (int x = 0; x <= 299; x++) {
        cout << "X=" << x << endl;
        for (int y = 0; y <= 299; y++) {
            int total = 0;
            for (int size = 1; size <= min(300-x,300-y); size++) {
                for (int i = 0; i < size; i++) {
                    total += cells[x+i][y+size-1];
                }
                for (int j = 0; j < size-1; j++) {
                    total += cells[x+size-1][y+j];
                }

                if (total > m) {
                    m = total;
                    mx = x;
                    my = y;
                    ms = size;
                }
            }
        }
    }
    cout << m << " " << mx << " " << my << " " << ms << endl;
}
