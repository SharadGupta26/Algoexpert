//https://leetcode.com/problems/sum-of-two-integers/description/

class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int temp = a ^ b;
            b = (a & b) << 1;
            a = temp;
        }   
    return a;
    }
}