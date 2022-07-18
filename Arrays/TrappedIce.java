/* Problem Name is &&& Snowpack &&& PLEASE DO NOT REMOVE THIS LINE. */

/*
** Instructions to candidate.
**  1) Given an array of non-negative integers representing the elevations
**     from the vertical cross section of a range of hills, determine how
**     many units of snow could be captured between the hills. 
**
**     See the example array and elevation map below.
**                                 ___
**             ___                |   |        ___
**            |   |        ___    |   |___    |   |
**         ___|   |    ___|   |   |   |   |   |   |
**     ___|___|___|___|___|___|___|___|___|___|___|___
**     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}
**                                 ___
**             ___                |   |        ___
**            |   | *   *  _*_  * |   |_*_  * |   |
**         ___|   | *  _*_|   | * |   |   | * |   |

**     ___|___|___|_*_|___|___|_*_|___|___|_*_|___|___
**     {0,  1,  3,  0,  1,  2,  0,  4,  2,  0,  3,  0}

       {0,  1,  3,  0,  0,  2,  0,  1 }
**
**     Solution: In this example 13 units of snow (*) could be captured.
**  
**  2) Consider adding some additional tests in doTestsPass().
**  3) Implement computeSnowpack() correctly.
*/

import java.io.*;
import java.util.*;

class Solution {
    /*
     ** Find the amount of snow that could be captured.
     */
    public static Integer computeSnowpack(Integer[] arr) {
        int snow = 0;
        for (int i = 0; i < arr.length;) {
            int left = calculateLeft(arr, i);
            if (left == arr.length) {
                System.out.println(snow);
                return snow;
            }
            int right = calculateRight(arr, left);
            System.out.println(arr[left] + " " + arr[right]);
            snow += compute(arr, left, right);

            i = right;
        }
        // System.out.println(snow);
        return snow;
    }

    private static Integer compute(Integer[] arr, int left, int right) {
        int snow = 0;
        for (int i = left + 1; i < right; i++) {
            snow += (Integer.min(arr[left], arr[right])) - arr[i];
        }
        return snow;
    }

    private static Integer calculateRight(Integer[] arr, int left) {
        int max = 0;
        int j = arr.length - 1;
        for (int i = left + 1; i < arr.length; i++) {
            if (arr[i] >= arr[left]) {
                return i;
            } else if (arr[i] > max) {
                max = arr[i];
                j = i;
            }
        }
        return j;
    }

    private static Integer calculateLeft(Integer[] arr, int i) {

        for (int j = i; j < arr.length - 1; j++) {
            if (arr[j + 1] < arr[j]) {
                return j;
            }
        }
        return arr.length;
    }

    /*
     ** Returns true if the tests pass. Otherwise, returns false;
     */
    public static boolean doTestsPass() {
        boolean result = true;
        result &= computeSnowpack(new Integer[] { 0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 0 }) == 13;
        result &= computeSnowpack(new Integer[] { 0, 1, 3, 0, 1, 2, 0, 4, 2, 0, 3, 5 }) == 16;
        result &= computeSnowpack(new Integer[] { 1, 1, 1, 1 }) == 0;

        return result;
    }

    /*
     ** Execution entry point.
     */
    public static void main(String[] args) {
        if (doTestsPass()) {
            System.out.println("All tests pass");
        } else {
            System.out.println("Tests fail.");
        }
    }
}
