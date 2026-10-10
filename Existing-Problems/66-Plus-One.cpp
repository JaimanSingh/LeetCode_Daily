class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        for (int i = n-1; i>=0; i--) {
            if (i == n-1)
                digits[i]++;
            if (digits[i]==10) {
                digits[i] = 0;
                if (i!=0) {
                    digits[i-1]++;
                }
                else{
                    digits.push_back(0);
                    digits[i] = 1;
                }
            }
        }
        return digits;
    }
};

// Detailed Explanation:
// Step 1:
// int n = digits.size();

// This initializes n to the size of the digits vector, i.e., the number of digits in the number.
// Step 2:
// for (int i = n-1; i >= 0; i--)

// This loop starts from the last digit (n-1, the least significant digit) and moves backward through the vector until it reaches the first digit (index 0).
// Step 3:
// if (i == n-1) digits[i]++;

// On the first iteration (when i == n-1), the last digit is incremented by 1 because we're adding 1 to the number.
// Step 4:
// if (digits[i] == 10)

// After incrementing the digit, if the current digit becomes 10 (because we carried over a value, e.g., 9 + 1 = 10), we need to handle the carry.
// Step 5:
// digits[i] = 0;

// Since the digit can't be 10 (digits can only be between 0 and 9), we set the current digit to 0 and prepare to carry 1 to the previous digit.
// Step 6 & Step 7:
// if (i != 0) { digits[i-1]++; }

// If we are not at the first digit (i != 0), we increment the previous digit (i-1) by 1 to handle the carry.
// Step 8, Step 9 & Step 10:
// else { digits.push_back(0); digits[i] = 1; }

// If we are at the first digit (i == 0), and a carry is still needed, this means the number has grown in size (e.g., 999 + 1 = 1000). We append a 0 to the end of the vector and set the first digit (digits[0]) to 1, representing the new leading digit.
// Step 11:
// return digits;

// After processing all the digits and handling any carry, we return the modified digits vector.