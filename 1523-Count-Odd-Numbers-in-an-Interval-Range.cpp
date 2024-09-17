//My Solution: MEMORY LIMIT EXCEEDED.`
// class Solution {
// public:
//     int countOdds(int low, int high) {
//         vector<int> odd;
//         vector<int> even;
//         for (int i = low; i <= high; i++) {
//             if (i % 2 == 0) {
//             even.push_back(i);
//         }
//         else {
//             odd.push_back(i);
//         }
//         }
//         return odd.size();
//     }
// };


class Solution {
public:
    int countOdds(int low, int high) {
        int count_odd = 0;
        for (int i = low; i <= high; i++) {
            if (i%2 != 0) {
                count_odd++;
            }
        }
        return count_odd;
    }
};