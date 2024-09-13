class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0 , j = 0; //INT I,J=0 SAHI NAHI HAI!!
        string ans = "";
        int n = word1.length();
        int m = word2.length();
        // int m = length(word2); --> YE NAHI HOTA. IT IS WORD1.LENGTH()

        while ((i<n) && (j<m)) {
            ans += word1[i];
            ans += word2[j];
            i++;
            j++;
        }

        while (i<n) {
            ans += word1[i];
            i++;
        }
        while (j<m) {
            ans += word2[j];
            j++;
        }

        return ans;
    }
};