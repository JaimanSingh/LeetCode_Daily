class Solution {
public:
    char findTheDifference(string s, string t) {

            int n = s.length();
            int m = t.length();
            sort(s.begin(), s.end());
            sort(t.begin(), t.end());
            for (int i = 0; i<n; i++) {
                if (s[i] != t[i]){
                    return t[i];
                }
            }
            return t.back(); //returns the last element in the container. 
            //THIS STATEMENT MEANS KI AGAR PEHLE WALON MEI DIFFERENT ELEMENT NAHI MILA TOH LAST MEI PAKKA HOGA TOH RETURN IT. 

        }
};