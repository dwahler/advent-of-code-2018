#include "util.hpp"

using namespace std;

typedef util::point<int> point;

int main() {
    const regex pattern("([0-9]+), ([0-9]+)");

    vector<point> points;

    int minx = 999999, maxx = -999999, miny = 999999, maxy = -999999;

    for (string l : util::lines(cin)) {
        smatch m = util::rmatch(l, pattern);
        point p = {stoi(m[1]), stoi(m[2])};
        
        minx = min(minx, p.x);
        maxx = max(maxx, p.x);
        miny = min(miny, p.y);
        maxy = max(maxy, p.y);

        points.push_back(p);
    }
    cout << minx << "," << maxx << "," << miny << "," << maxy << endl;

    unordered_map<int, int> counts;
    unordered_set<int> infinite;

    for (int x = minx; x <= maxx; x++) {
        for (int y = miny; y <= maxy; y++) {
            int mindist = 999999;
            int idx = -1;
            for (int i = 0; i < points.size(); i++) {
                int d = abs(x-points[i].x)+abs(y-points[i].y);
                if (d < mindist) {
                    mindist = d;
                    idx = i;
                } else if (d == mindist) {
                    idx = -1;
                }
            }
            if (idx == -1) continue;

            if (x == minx || x == maxx || y == miny || y == maxy) {
                infinite.insert(idx);
            }
            counts[idx]++;
        }
    }

    int max_value = -1;
    for (auto& it : counts) {
        if (infinite.count(it.first) == 0) {
            max_value = max(max_value, it.second);
        }
    }
    cout << "part 1: " << max_value << endl;

    int safe_count = 0;
    for (int x = minx; x <= maxx; x++) {
        for (int y = miny; y <= maxy; y++) {
            ll d = 0;
            for (point& p : points) {
                d += abs(x-p.x)+abs(y-p.y);
            }
            if (d < 10000) {
                safe_count++;
            }
        }
    }
    cout << "part 2: " << safe_count << endl;
}
