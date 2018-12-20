#include "util.hpp"

using namespace std;

#define addi(a,b,c) (regs[c] = regs[a]+b)
#define seti(a,b,c) (regs[c] = a)
#define mulr(a,b,c) (regs[c] = regs[a]*regs[b])
#define eqrr(a,b,c) (regs[c] = (regs[a]==regs[b] ? 1 : 0))
#define addr(a,b,c) (regs[c] = regs[a]+regs[b])
#define gtrr(a,b,c) (regs[c] = (regs[a]>regs[b] ? 1 : 0))
#define muli(a,b,c) (regs[c] = regs[a]*b)
#define setr(a,b,c) (regs[c] = regs[a])

int main() {
    vector<long long> regs(6,0);
    regs[0] = 1;
    int ip=0;
    long long inscount = 0;

    while (true) {
        regs[2] = ip;

        if (inscount % 10000000 == 0) {
            cout << inscount << " " << regs << endl;
        }
    
        switch (ip) {
            case 0: addi(2,16,2); break;
            case 1: seti(1,0,1); break;
            case 2: seti(1,4,3); break;
            case 3: mulr(1,3,4); break;
            case 4: eqrr(4,5,4); break;
            case 5: addr(4,2,2); break;
            case 6: addi(2,1,2); break;
            case 7: addr(1,0,0); break;
            case 8: addi(3,1,3); break;
            case 9: gtrr(3,5,4); break;
            case 10: addr(2,4,2); break;
            case 11: seti(2,5,2); break;
            case 12: addi(1,1,1); break;
            case 13: gtrr(1,5,4); break;
            case 14: addr(4,2,2); break;
            case 15: seti(1,1,2); break;
            case 16: mulr(2,2,2); break;
            case 17: addi(5,2,5); break;
            case 18: mulr(5,5,5); break;
            case 19: mulr(2,5,5); break;
            case 20: muli(5,11,5); break;
            case 21: addi(4,5,4); break;
            case 22: mulr(4,2,4); break;
            case 23: addi(4,9,4); break;
            case 24: addr(5,4,5); break;
            case 25: addr(2,0,2); break;
            case 26: seti(0,0,2); break;
            case 27: setr(2,3,4); break;
            case 28: mulr(4,2,4); break;
            case 29: addr(2,4,4); break;
            case 30: mulr(2,4,4); break;
            case 31: muli(4,14,4); break;
            case 32: mulr(4,2,4); break;
            case 33: addr(5,4,5); break;
            case 34: seti(0,6,0); break;
            case 35: seti(0,3,2); break;
            default: cout << regs << endl; return 0;
        }

        ip = regs[2];
        ip++;
        inscount++;
    }
}
