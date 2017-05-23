#include <stdio.h>
#include <math.h>
#include <cs50.h>

int main(void){
    int coins = 0;
    float change = GetFloat();
    while (change < 0) {
        printf("What your change? \n");
        change = GetFloat();
    int dec =  round(change * 100);
    while (dec > 0) {
        if ((dec - 25) >= 0)
            { dec = dec - 25; coins++; };
        else if ((dec - 10) >= 0) 
            { dec = dec - 10; coins++; };
        else if ((dec - 5) >= 0) 
            { dec = dec - 5; coins++; };
        else if ((dec - 1) >= 0) 
            { dec = dec - 1; coins++; };
    }
    printf("%d\n", coins);
}