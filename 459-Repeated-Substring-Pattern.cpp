class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int len = s.length();  // Store the length of the string

        // Loop through possible substring lengths
        for (int i = 1; i <= len / 2; i++) {
            if (len % i == 0) {  // Check if the current `i` divides the string length perfectly
                string substring = s.substr(0, i);  // Extract substring of length `i`
                string repeated = "";
                
                // Repeat the substring `len / i` times to form a new string
                for (int j = 0; j < len / i; j++) {
                    repeated += substring;
                }
                
                // If the repeated string matches the original string `s`, return true
                if (repeated == s) return true;
            }
        }
        
        // If no valid repeated substring pattern is found, return false
        return false;
    }
};
