#include <iostream>
#include <stdio.h>
#include <vector>
#include <ctime>

using namespace std;

/*
 * Returns true if this array is big enough
 */
bool isCorrectSize(char* n)
{
    return n[0] != 0;
}

void addNums(char* n1, char* n2, char* result)
{
    // just to make sure there aren't residual numbers still in there
    for (int i=0; i<1000; i++) result[i] = 0;
    // iterate over each digit in each number
    for (int i=999; i>=0; i--)
    {
        // add!
        int sum = n1[i] + n2[i] + result[i];
        int carry = sum / 10;
        int carryLoc = i-1;
        sum %= 10;
        result[i] = (char)sum;
        while (carryLoc >= 0 && carry > 0) {
            char toStore = carry % 10;
            result[carryLoc] += toStore;
            carry /= 10;
            carryLoc -= 1;
        }
    }
}

/*
 * Get an array of chars that will be used to represent a very large number
 * also store an initial value 'start' in the array
 * NOTE: start must be on the interval [0, 9]
 */
char* getNumArray(int start) {
    char* ret = new char[1000];
    for (int i=0; i<1000; i++)
    {
        ret[i] = 0;
    }
    ret[999] = start;
    return ret;
}

int getIndexOfFib1000Digits()
{
    int i = 2;
    char* f1 = getNumArray(1);
    char* f2 = getNumArray(1);
    char* tmp = getNumArray(0);
    while (!isCorrectSize(f2)) {
        addNums(f1, f2, tmp);
        // shuffle all the pointers up one
        char* tmp2 = f1;
        f1 = f2;
        f2 = tmp;
        tmp = tmp2;
        i++;
    }
    return i;
}

int main()
{
    clock_t begin = clock();
    printf("Answer: %d\n", getIndexOfFib1000Digits());
    clock_t end = clock();
    double seconds = double(end - begin) / CLOCKS_PER_SEC;
    printf("%0.4f seconds\n", seconds);
}
