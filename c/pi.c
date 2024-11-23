#include <stdio.h>

int factorial(int number){

    if (number != 0){
        int i = number - 1;
        int r = number;
        while (i > 0){
            r = r*i;
            i = i - 1;
        }
        return r;
    }
    else{
        return 1;
    }
}

double sine(double number){
    int running = 1;
    int sinn = 0;
    double sineSum = 0;\

    while (running == 1){
        
    }
}

int main(){

    int n = 0;

    //int sineOfN = sine(n);

    //printf("Factorial of %d is %d\n", n, fact);
    return 0;
}