#pragma once

#include <iostream>
#include <regex>
#include <vector>
#include <string>
#include <iterator>
#include <tuple>
#include <unordered_map>
#include <map>
#include <set>
#include <unordered_set>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <queue>

namespace util {
    using namespace std;

    class line : public string {};

    istream& operator>>(istream& is, line &l) {
        getline(is, l);
        return is;
    }

    class istream_lines {
        istream& is;

        public:
        istream_lines(istream& is) : is(is) { }

        istream_iterator<line> begin() {
            return istream_iterator<line>(is);
        }

        istream_iterator<line> end() {
            return istream_iterator<line>();
        }
    };

    istream_lines lines(istream& is) {
        return istream_lines(is);
    }

    smatch rmatch(const string& text, const regex& pattern) {
        smatch m;
        if (!regex_match(text, m, pattern)) {
            throw invalid_argument("match failure");
        }
        return m;
    }

    template <typename T>
    struct point {
        T x;
        T y;

        point(const T& x, const T& y) : x(x), y(y) { }
        point() { }
    };

    template <typename T>
    std::ostream& operator<<(std::ostream& os, const point<T>& p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }

}

    template <typename T>
    std::ostream& operator<<(std::ostream& os, const std::vector<T>& v) {
        os << "[";
        for (int i = 0; i < v.size(); i++) {
            if (i > 0) {
                os << ", ";
            }
            os << v[i];
        }
        os << "]";
        return os;
    }

template <typename K, typename V>
std::ostream& operator<<(std::ostream& os, const std::unordered_map<K, V>& m) {
    os << "{";
    bool first = true;
    for (auto& it : m) {
        if (!first) { 
            os << ", ";
        } else {
            first = false;
        }
        os << it.first << ": " << it.second;
    }
    os << "}";
    return os;
}

template <typename K, typename V>
std::ostream& operator<<(std::ostream& os, const std::map<K, V>& m) {
    os << "{";
    bool first = true;
    for (auto& it : m) {
        if (!first) { 
            os << ", ";
        } else {
            first = false;
        }
        os << it.first << ": " << it.second;
    }
    os << "}";
    return os;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::unordered_set<T>& s) {
    os << "{";
    bool first = true;
    for (auto& it : s) {
        if (!first) { 
            os << ", ";
        } else {
            first = false;
        }
        os << it;
    }
    os << "}";
    return os;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, const std::set<T>& s) {
    os << "{";
    bool first = true;
    for (auto& it : s) {
        if (!first) { 
            os << ", ";
        } else {
            first = false;
        }
        os << it;
    }
    os << "}";
    return os;
}

typedef long long ll;
typedef unsigned long long ull;

