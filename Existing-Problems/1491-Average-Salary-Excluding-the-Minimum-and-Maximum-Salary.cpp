
class Solution {
public:
    double average(std::vector<int>& salary) {
        // Sort the array to easily remove the minimum and maximum
        std::sort(salary.begin(), salary.end());

        // Accumulate the sum excluding the first (min) and last (max) elements
        int sum = std::accumulate(salary.begin() + 1, salary.end() - 1, 0);

        // Calculate the average by dividing by the number of elements excluding min and max
        double average = sum / (salary.size() - 2.0);

        return average;
    }
};