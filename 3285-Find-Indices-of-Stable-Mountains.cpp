class Solution {
public:
    vector<int> stableMountains(vector<int>& height, int threshold) {
        vector<int> stable;  // Use a vector to store indices of stable mountains
        for (int i = 1; i < height.size(); i++) {  // Start from index 1 because mountain 0 is not stable
            if (height[i - 1] > threshold) {  // Check if the previous mountain is higher than the threshold
                stable.push_back(i);  // Add the index of the current mountain to the result
            }
        }
        return stable;  // Return the vector of stable mountain indices
    }
};
// class Solution {
// public:
//     vector<int> stableMountains(vector<int>& height, int threshold) {
//         vector<int> stable;
//         for (int i = 1; i <= height.size(); i++) {
//             if (height[i-1] >= threshold) {
//                 stable += height[i];  
//         }
//         }
//             return 0;
//     }
// };