1class Solution {
2public:
3    int reverse(int x) {
4        
5        int ans = 0;
6        while (x!=0) {
7
8            int digit = x%10;
9
10            if ((ans > INT_MAX/10) || (ans < INT_MIN/10)) {
11                return 0; 
12            }
13
14            ans = (ans*10) + digit;
15            x = x/10;
16        }
17        return ans;
18    }
19};