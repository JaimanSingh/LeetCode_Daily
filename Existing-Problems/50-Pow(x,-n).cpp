class Solution {
public:
    double myPow(double x, int n) {

        double ans = 1.0 ;
        long long num = n ; 
        if(num<0) num = -1* num; 

        while(num){
            if(num % 2){
                ans = ans*x;
                num = num -1; 
            }
            else{
                x = x*x; 
                num = num/2 ; 
            }
        }

        if(n<0 )  ans = (double)(1.0) / (double)(ans);  
        return ans ; 

    }
    };


//TLE
// class Solution {
// public:
//     double myPow(double x, int n) {
//             double ans = 1;
//             if (n<0) {
//                 n = -n;
//                 x = 1/x;
//             }
//             for (double i = 1; i<=n; i++) {
//                 ans*= x;
//             }
//             return ans;

//         }
//     };
