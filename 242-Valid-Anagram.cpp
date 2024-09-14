//FIRST SELF ATTEMPT QUESTION (WITH A LITTLE V MINOR RECITFICATION FROM CGT BUT YAYAY!!)
class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.length();
        int m = t.length();
        if (n!=m) {
            return false;
        }
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        for (int i = 0; i<m; i++) {
            if (s[i]!=t[i]){
                return false;
            }
        }
        return true;
    }
};