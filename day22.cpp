#include "util.hpp"

using namespace std;

const long long M=20183;

struct state {
    int x, y, tool;
}

int main() {
    long long depth = 10914;
    int tx = 9, ty = 739;

    vector<vector<long long>> grid(tx+1, vector<long long>(ty+1));
    grid[0][0] = 0;
    for (long long x = 1; x <= tx; x++) {
        grid[x][0] = (x*16807L)%M;
    }
    for (long long y = 1; y <= ty; y++) {
        grid[0][y] = (y*48271L)%M;
    }
    for (int x = 1; x <= tx; x++) {
        for (int y = 1; y <= ty; y++) {
            grid[x][y] = ((grid[x-1][y]+depth)*(grid[x][y-1]+depth))%M;
        }
    }
    grid[tx][ty] = 0;
    long long sum = 0;
    for (int x = 0; x <= tx; x++) {
        for (int y = 0; y <= ty; y++) {
            sum += ((grid[x][y]+depth)%M)%3;
        }
    }
    cout << sum << endl;

}
